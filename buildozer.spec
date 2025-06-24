[app]

# Nome visível no celular
title = BlazePreditivo

# Nome interno do pacote (sem espaços)
package.name = blaze_preditivo

# Domínio reverso (pode ser fictício)
package.domain = org.kivy

# Diretório com o código fonte
source.dir = .

# Extensões de arquivos incluídas no APK
source.include_exts = py,kv,png,jpg,ttf,xml,md,wav,ogg

# Versão do app
version = 1.0

# Arquivo principal do app
entrypoint = blaze_preditivo.py

# Bibliotecas necessárias
requirements = python3,kivy,requests,bs4,plyer

# Orientação do app
orientation = portrait

# Tela cheia
fullscreen = 1

# Ocultar barra de status (opcional)
android.hide_statusbar = 1

# Permissões necessárias no Android
android.permissions = INTERNET,VIBRATE

# API mínima e alvo (compatível com Android 5.0+ e SDK 31)
android.minapi = 21
android.api = 31
android.sdk = 31
android.ndk_api = 21

# O Buildozer baixa NDK antigo por padrão; você usa o 25b manualmente no GitHub Actions
# Então não defina a versão aqui — deixe o workflow controlar pelo ANDROID_NDK_HOME
# Se quiser forçar, descomente e use o caminho:
# android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b/android-ndk-r25b

# Arquitetura do dispositivo
arch = armeabi-v7a

# Nome do APK gerado em modo debug
android.debug.apk = BlazePreditivo.apk

# Copiar APK para a raiz do projeto após build
copy_to_current = 1

# Nível de log (2 = detalhado)
log_level = 2

# Ícone personalizado (caminho relativo ao projeto)
android.icon = icons/exu_tridente.png

# Evita usar build system antigo
use_legacy_setup_py = 1

# Bootstrap recomendado para apps Kivy
bootstrap = sdl2

# Desativa compilação do .py para .so (mais rápido em debug)
copy_libs = 1
