# 🏭 Гофроагрегат — Обучающий симулятор

> Интерактивный симулятор работы на гофроагрегате **Fosber** для обучения операторов.
> Позволяет отрабатывать нештатные ситуации без риска для реального оборудования.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Kivy](https://img.shields.io/badge/Kivy-2.3.0-green)
![Buildozer](https://img.shields.io/badge/Buildozer-1.5+-orange)
![Platform](https://img.shields.io/badge/Platform-Android-brightgreen)

---

## 📖 О проекте

**Гофроагрегат** — это обучающее приложение-симулятор, которое моделирует работу реальной линии по производству гофрокартона **Fosber** (пятислойка, 2 модуля гофрирования).

Приложение позволяет:
- 🎮 Отрабатывать штатные и нештатные ситуации
- 👷 Работать на разных участках: Модуль, Склейка, Релёвки, Хвост
- 📊 Следить за заказами, палетами и браком
- 🧠 Проходить викторины по своему участку
- 📡 Видеть случайные события: обрывы, поломки, смену бригад, "болтовню" в наушниках

---

## 🚀 Установка APK на Android

### Способ 1: Готовый APK (рекомендуется)

1. Перейдите в раздел [**Actions**](../../actions) репозитория
2. Выберите последний успешный workflow (зелёная галочка ✅)
3. Скачайте артефакт **`gofroagregat-apk`**
4. Распакуйте ZIP-архив → внутри файл `gofroagregat-1.0.0-debug.apk`
5. Перекиньте APK на телефон и установите

### Способ 2: Локальная сборка

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/Ostenvrn/gofroagregat.git
cd gofroagregat

# 2. Установите зависимости (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y \
    git zip unzip openjdk-17-jdk \
    autoconf libtool pkg-config \
    zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 \
    cmake libffi-dev libssl-dev

# 3. Создайте виртуальное окружение
python3 -m venv venv
source venv/bin/activate

# 4. Установите Buildozer и Cython
pip install --upgrade pip
pip install buildozer cython

# 5. Соберите APK
export P4A_IGNORE_RECIPES=libthorvg
buildozer android debug

# APK появится в папке: bin/gofroagregat-1.0.0-debug.apk
