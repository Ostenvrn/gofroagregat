[app]
title = Гофроагрегат
package.name = gofroagregat
package.domain = org.ostenvrn

source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json,md

requirements = python3==3.9,kivy==2.3.1,cython==0.29.33,legacy-cgi

orientation = portrait
fullscreen = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 24

# Графика
android.graphics = yes
# Увеличение памяти
android.maxsdk = 33

# Отключить Cython (для скорости)
android.add_src =

[buildozer]
log_level = 2
warn_on_root = 1
