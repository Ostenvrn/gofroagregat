[app]
title = Гофроагрегат
package.name = gofroagregat
package.domain = org.ostenvrn

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json,md

version = 1.0.0

# ===== НОВЫЕ НАСТРОЙКИ =====
p4a.branch = develop

requirements = python3==3.11.7,kivy==2.3.1,jnius==1.4.0,cython==3.0.11

orientation = portrait
fullscreen = 1

android.permissions = INTERNET
android.api = 35
android.sdk = 35
android.minapi = 24
android.ndk = 28b

android.graphics = yes
android.maxsdk = 35
android.add_src =

[buildozer]
log_level = 2
warn_on_root = 1
