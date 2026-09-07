FROM kivy/buildozer:latest

# Устанавливаем переменные окружения
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow

# Рабочая директория
WORKDIR /home/user/build
