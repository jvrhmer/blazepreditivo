[app]

# Nome do aplicativo
title = BlazePreditivo

# Nome do pacote (interno)
package.name = blaze_preditivo

# Domínio do pacote (reverso, fictício)
package.domain = org.kivy

# Código-fonte
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,xml,md,wav,ogg

# Versão do app
version = 1.0

# Arquivo principal de entrada
entrypoint = blaze_preditivo.py

# Bibliotecas necessárias (PyPI + libs Android)
requirements = python3,kivy,requests,bs4,plyer

# Modo retrato
orientation = portrait

# Tela cheia e sem barra de status
fullscreen = 1
android.hide_statusbar = 1

# Permissões necessárias para funcionamento
android.permissions = INTERNET,VIBRATE

# Versões da API e ferramentas do Android
android.minapi = 21
android.api = 31
android.build_tools_version = 31.0.0
android.ndk = 25b
android.archs = armeabi-v7a

# Caminhos fixos do SDK e NDK (evita download automático)
android.sdk_path = .buildozer/android/platform/android-sdk
android.ndk_path = .buildozer/android/platform/android-ndk-r25b

# Nome do APK gerado
android.debug.apk = BlazePreditivo.apk

# Copia APK gerado para o diretório raiz do projeto
copy_to_current = 1

# Nível de log do buildozer
log_level = 2

# Ícone do app
android.icon = icons/exu_tridente.png
