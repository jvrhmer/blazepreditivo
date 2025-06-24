[app]

# Nome do seu app
title = BlazePreditivo

# Nome do pacote - mude para algo seu (inverso do domínio)
package.name = blazepreditivo
package.domain = org.example

# Versão do app
version = 1.0

# Arquivo principal do seu app
source.include_exts = py,png,jpg,kv,atlas,json
source.dir = .

# Arquivo Python principal
entrypoint = main.py

# Permissões extras (se precisar)
# android.permissions = INTERNET

# Orientação da tela: portrait (vertical)
orientation = portrait

# Pacotes Python extras que seu app usa
requirements = python3,kivy,requests

# Para buildozer reconhecer build-tools versão fixa:
android.sdk = 33
android.build_tools_version = 33.0.2

# Versão mínima do Android suportada
android.minapi = 21

# Versão target do Android
android.target = 33

# Permitir tela cheia
fullscreen = 0

# Versão do NDK (use automático do buildozer)
# android.ndk = 25b

# Adiciona suporte a OpenGL ES 2.0 (default)
# android.opengl = es2

[buildozer]

# Local para armazenar os builds
build_dir = .buildozer