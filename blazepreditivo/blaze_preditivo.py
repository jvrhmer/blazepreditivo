# blaze_preditivo.py
import requests
from bs4 import BeautifulSoup
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from plyer import vibrator, notification
from threading import Thread
import collections

KV = '''
<MainWidget>:
    orientation: 'vertical'
    padding: 10
    spacing: 10
    canvas.before:
        Color:
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        id: status_label
        text: "Carregando resultados..."
        color: 1, 1, 1, 1
        font_size: 18

    Label:
        id: recent_results
        text: ""
        color: 1, 1, 1, 1

    Label:
        id: pattern_label
        text: ""
        color: 1, 0, 0, 1
        font_size: 20

    Label:
        id: prediction_label
        text: ""
        color: 1, 1, 1, 1
        font_size: 18

    Label:
        id: stats_label
        text: ""
        color: 0, 1, 0, 1
        font_size: 16
'''

def mapear_cor(numero):
    if numero == 0:
        return 'W'
    elif 1 <= numero <= 7:
        return 'R'
    elif 8 <= numero <= 14:
        return 'B'
    return '?'

class MainWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.resultados = []
        Clock.schedule_interval(lambda dt: Thread(target=self.atualizar).start(), 15)

    def obter_cores(self):
        url = "https://historicosblaze.com/blaze/doubles"
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.text, 'html.parser')
            divs = soup.find_all("div", class_="number")
            numeros = [int(div.text.strip()) for div in divs if div.text.strip().isdigit()]
            return [mapear_cor(n) for n in numeros]
        except Exception as e:
            return []

    def encontrar_padrao(self, cores):
        padroes = collections.defaultdict(list)
        for tam in range(3, 11):
            for i in range(len(cores) - tam - 2):
                chave = ''.join(cores[i:i+tam])
                proximo = cores[i+tam+1]
                padroes[(chave, tam)].append(proximo)

        melhores = {}
        for (chave, tam), valores in padroes.items():
            if len(valores) >= 10:
                mais_comum, cont = collections.Counter(valores).most_common(1)[0]
                acuracia = cont / len(valores)
                if acuracia >= 0.9:
                    melhores[(chave, tam)] = (mais_comum, acuracia, len(valores))
        return melhores

    def atualizar(self):
        cores = self.obter_cores()
        if not cores:
            return
        self.resultados = cores
        padroes = self.encontrar_padrao(cores)
        melhor = max(padroes.items(), key=lambda x: x[0][1], default=None)

        def ui():
            self.ids.status_label.text = "Atualizado"
            self.ids.recent_results.text = ' '.join([{'R':'🔴','B':'⚫','W':'⬜'}.get(c,'?') for c in cores[:30]])
            if melhor:
                seq, (prev, acc, qtd) = melhor
                self.ids.pattern_label.text = f"Padrão ({len(seq)}): {seq}"
                self.ids.prediction_label.text = f"Previsão 2ª cor: {prev}"
                self.ids.stats_label.text = f"Acurácia: {acc*100:.1f}%, Ocorrências: {qtd}"
                vibrator.vibrate(0.5)
                notification.notify(title="BlazePreditivo", message=f"Padrão {seq} → {prev}")
            else:
                self.ids.pattern_label.text = "Nenhum padrão forte"
                self.ids.prediction_label.text = ""
                self.ids.stats_label.text = ""

        Clock.schedule_once(lambda dt: ui())

class BlazePreditivoApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#000000')
        Builder.load_string(KV)
        return MainWidget()

if __name__ == '__main__':
    BlazePreditivoApp().run()
