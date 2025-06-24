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

# API mínima do Android (21 = Android 5.0)
android.minapi = 21

# API alvo (30 = Android 11)
android.api = 30

# NDK (compatível com o GitHub Actions e maioria dos builds)
android.ndk = 21b

# Arquitetura do dispositivo
android.arch = armeabi-v7a

# Nome do APK gerado
android.debug.apk = BlazePreditivo.apk

# Após o build, copie o APK para a raiz
copy_to_current = 1

# Habilitar logs durante a execução no Android
log_level = 2

# Descomente e configure se quiser ícone personalizado
android.icon = icons/exu_tridente.png
