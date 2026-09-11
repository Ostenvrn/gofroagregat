[app]

title = Гофроагрегат
package.name = gofroagregat
package.domain = org.ostenvrn

version = 1.0.0

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json,md
source.exclude_exts = pyc,pyo,so,o,obj,class,dbg,pycache

# ===== Requirements =====
requirements = python3,kivy==2.3.0,jnius,pyjnius

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

# ===== Фиксируем p4a на стабильный релиз =====
p4a.branch = v2024.01.21

# ===== Debug-сборка делает APK, AAB отключён =====
# android.export_aab = True

[buildozer]
log_level = 2
warn_on_root = 0
