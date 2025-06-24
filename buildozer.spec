[app]

# Nome visível no celular
title = BlazePreditivo

# Nome interno do pacote
package.name = blaze_preditivo

# Domínio reverso (pode ser fictício)
package.domain = org.kivy

# Código fonte
source.dir = .

# Arquivo principal do app
entrypoint = blaze_preditivo.py

# Extensões incluídas
source.include_exts = py,kv,png,jpg,ttf,xml,md,wav,ogg

# Versão
version = 1.0

# Requisitos (Python e libs)
requirements = python3,kivy,requests,bs4,plyer

# Bootstrap (recomendado para Kivy)
bootstrap = sdl2

# Tela e orientação
orientation = portrait
fullscreen = 1
android.hide_statusbar = 1

# Permissões necessárias
android.permissions = INTERNET,VIBRATE

# API mínima e alvo (compatível com GitHub Actions e SDK/NDK configurados)
android.minapi = 21
android.api = 31
android.sdk = 31
android.ndk_api = 21

# Arquitetura
arch = armeabi-v7a

# Nome do APK de debug
android.debug.apk = BlazePreditivo.apk

# Copia o APK final para a raiz do projeto após o build
copy_to_current = 1

# Nível de log detalhado (2 = debug completo)
log_level = 2

# Ícone (opcional, certifique-se de que o caminho exista)
android.icon = icons/exu_tridente.png

# Otimizações para build
use_legacy_setup_py = 1
copy_libs = 1