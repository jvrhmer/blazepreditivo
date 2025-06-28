[app]

# Nome do seu app
title = BlazePreditivo

# Nome do pacote
package.name = blazepreditivo
package.domain = org.example

# Versão do app
version = 1.0

# Extensões de arquivos a incluir
source.include_exts = py,png,jpg,kv,atlas,json
source.dir = .

# Arquivo principal
entrypoint = blaze_preditivo.py

# Orientação da tela
orientation = portrait

# Permissões necessárias
android.permissions = INTERNET, VIBRATE, RECEIVE_BOOT_COMPLETED

# Bibliotecas Python utilizadas
requirements = python3,kivy,requests,plyer,beautifulsoup4

# Versões do SDK e Build Tools
android.sdk = 33
android.build_tools_version = 33.0.2

# API mínima e alvo
android.minapi = 21
android.target = 33

# Tela cheia
fullscreen = 0

[buildozer]

# Pasta de build
build_dir = .buildozer
