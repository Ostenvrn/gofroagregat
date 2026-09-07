FROM kivy/buildozer:latest

# Отключаем интерактивные диалоги
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow

# Копируем патч внутрь контейнера
COPY fix_libthorvg.patch /tmp/fix_libthorvg.patch

# Применяем патч к python-for-android
RUN cd /home/user/.buildozer/android/platform/python-for-android && \
    patch -p1 < /tmp/fix_libthorvg.patch || true

# Рабочая директория
WORKDIR /home/user/hostcwd

CMD ["buildozer", "android", "debug"]
