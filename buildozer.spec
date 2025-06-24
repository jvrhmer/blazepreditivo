[app]

title = BlazePreditivo
package.name = blaze_preditivo
package.domain = org.kivy

source.dir = .
source.include_exts = py,kv,png,jpg,ttf,xml,md,wav,ogg

version = 1.0
entrypoint = blaze_preditivo.py

requirements = python3,kivy,requests,bs4,plyer

orientation = portrait
fullscreen = 1
android.hide_statusbar = 1
android.permissions = INTERNET,VIBRATE

android.minapi = 21
android.api = 31
android.build_tools_version = 31.0.0
android.ndk = 25b
android.archs = armeabi-v7a

android.debug.apk = BlazePreditivo.apk
copy_to_current = 1

log_level = 2

android.icon = icons/exu_tridente.png
