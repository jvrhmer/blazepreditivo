[app]

# Nome visível no app
title = BlazePreditivo

# Nome do pacote
package.name = blaze_preditivo

# Domínio reverso
package.domain = org.kivy

# Diretório do código
source.dir = .

# Arquivo principal
entrypoint = blaze_preditivo.py

# Extensões incluídas no APK
source.include_exts = py,kv,png,jpg,ttf,xml,md,wav,ogg

# Versão
version = 1.0

# Requisitos do app
requirements = python3,kivy,requests,bs4,plyer

# Bootstrap gráfico
bootstrap = sdl2

# Orientação e tela cheia
orientation = portrait
fullscreen = 1
android.hide_statusbar = 1

# Permissões necessárias
android.permissions = INTERNET,VIBRATE

# Versões mínimas e alvo do Android
android.minapi = 21
android.api = 31
android.sdk = 31
android.ndk_api = 21

# Nome do APK
android.debug.apk = BlazePreditivo.apk

# Arquitetura suportada
arch = armeabi-v7a

# Copiar APK para o diretório atual após build
copy_to_current = 1

# Log detalhado
log_level = 2

# Ícone do app (verifique se o caminho está certo)
android.icon = icons/exu_tridente.png

# Usa libs em tempo de execução
copy_libs = 1

# ⚠️ Adição fundamental para apontar SDK/NDK personalizados
[buildozer]
android.sdk_path = .buildozer/android/platform/android-sdk
android.ndk_path = .buildozer/android/platform/android-ndk-r25b
