[app]

# ============================================================
# ОСНОВНАЯ ИНФОРМАЦИЯ О ПРИЛОЖЕНИИ
# ============================================================
title = Гофроагрегат
package.name = gofroagregat
package.domain = org.ostenvrn

version = 1.0.0

# ============================================================
# ИСХОДНЫЙ КОД
# ============================================================
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,json,md
source.exclude_exts = pyc,pyo,so,o,obj,class,dbg,pycache

# ============================================================
# ЗАВИСИМОСТИ (указаны точные версии для стабильности)
# ============================================================
requirements = python3==3.11.7,kivy==2.3.1,jnius==1.4.0,cython==3.0.11

# ============================================================
# НАСТРОЙКИ ЭКРАНА
# ============================================================
orientation = portrait
fullscreen = 1

# ============================================================
# ИКОНКА ПРИЛОЖЕНИЯ
# ============================================================
# Поместите файл icon.png (размер 512x512) в папку с проектом
icon.filename = %(source.dir)s/icon.png

# ============================================================
# РАЗРЕШЕНИЯ ANDROID
# ============================================================
android.permissions = INTERNET, VIBRATE, WAKE_LOCK, ACCESS_NETWORK_STATE
android.manifest.add_application_meta_data = 
android.manifest.add_to_application = 

# ============================================================
# ANDROID SDK / NDK / API (стабильные версии)
# ============================================================
android.api = 33
android.sdk = 33
android.minapi = 24
android.ndk = 25b
android.maxsdk = 33
android.target_sdk = 33
android.accept_sdk_license = yes

# ============================================================
# ПАРАМЕТРЫ СБОРКИ (Python-for-Android)
# ============================================================
p4a.branch = master
android.export_aab = False
p4a.local_recipes = 
android.gradle_dependencies = 
android.add_src = 
android.graphics = yes
android.extra_java_dirs = 
android.extra_jar_dirs = 
android.extra_javac_options = 
android.use_gradle = yes

# ============================================================
# ОПЦИОНАЛЬНО: ИСКЛЮЧЕНИЕ ФАЙЛОВ ИЗ APK
# ============================================================
android.exclude_activities = 
android.ignore_activity_not_found = yes
android.blacklist_activities = 

# ============================================================
# ПАРАМЕТРЫ РАЗВЕРТКИ (для приложений с камерой/видео)
# ============================================================
# camera = 0
# videoplayer = 0
# android.min_camera_api = 

# ============================================================
# ПРИМЕР: ДОБАВЛЕНИЕ СВОИХ ФАЙЛОВ В APK
# ============================================================
# android.add_src = path/to/your/source
# android.add_assets = path/to/assets

[buildozer]
log_level = 2
warn_on_root = 1
