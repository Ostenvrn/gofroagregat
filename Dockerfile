FROM kivy/buildozer:latest

# Отключаем интерактивные диалоги
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow

# Создаём пользователя (если его нет)
RUN useradd -m -s /bin/bash user 2>/dev/null || true

# НЕ меняем владельца! Просто создаём папку
RUN mkdir -p /home/user/.buildozer

# Рабочая директория
WORKDIR /home/user/build

CMD ["bash"]
