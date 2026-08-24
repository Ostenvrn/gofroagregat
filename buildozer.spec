[app]
title = Гофроагрегат
package.name = gofroagregat
package.domain = org.ostenvrn

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json,md

version = 1.0.0

requirements = python3==3.9.25,kivy==2.3.1,cython==0.29.33,legacy-cgi

orientation = portrait
fullscreen = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 24

android.graphics = yes
android.maxsdk = 33
android.add_src =

[buildozer]
log_level = 2
warn_on_root = 1
