[app]

title = Гофроагрегат
package.name = gofroagregat
package.domain = org.ostenvrn

version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json,md
source.exclude_exts = pyc,pyo,so,o,obj,class,dbg,pycache

# ===== ФИКСИРУЕМ ТОЧНЫЕ ВЕРСИИ =====
# Cython 0.29.36 — существует и работает с Kivy 2.1.0
# pyjnius добавлен без версии
requirements = python3,kivy==2.1.0,jnius,pyjnius,cython==0.29.36

orientation = portrait
fullscreen = 1

icon.filename = %(source.dir)s/icon.png

android.permissions = INTERNET, VIBRATE, WAKE_LOCK
android.api = 33
android.sdk = 33
android.minapi = 24
android.ndk = 25b
android.maxsdk = 33
android.target_sdk = 33
android.accept_sdk_license = yes

# ===== ФИКСИРУЕМ ВЕТКУ P4A =====
p4a.branch = master
android.export_aab = True

[buildozer]
log_level = 2
warn_on_root = 0
