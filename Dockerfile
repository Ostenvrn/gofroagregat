FROM ubuntu:22.04

# Отключаем интерактивные диалоги
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    sudo git zip unzip openjdk-17-jdk \
    python3-pip python3-dev python3-venv \
    autoconf libtool pkg-config zlib1g-dev libncurses-dev \
    cmake libffi-dev libssl-dev automake \
    libsdl2-dev libsdl2-ttf-dev libsdl2-mixer-dev libsdl2-image-dev \
    make build-essential wget curl software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Python 3.9.19 через deadsnakes
RUN add-apt-repository -y ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.9 python3.9-dev python3.9-venv && \
    rm -rf /var/lib/apt/lists/*

# ЗАМЕНЯЕМ СИСТЕМНЫЙ PYTHON НА PYTHON 3.9
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1 && \
    update-alternatives --set python3 /usr/bin/python3.9

# Проверяем версию
RUN python3 --version

# Устанавливаем Buildozer и конкретную версию python-for-android
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install buildozer cython && \
    python3 -m pip install --upgrade python-for-android==2024.1.21

# Создаём пользователя
RUN useradd -m -s /bin/bash user && echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER user
WORKDIR /home/user/build

CMD ["bash"]
