FROM ubuntu:22.04

# Устанавливаем переменные
ENV DEBIAN_FRONTEND=noninteractive
ENV USER=user
ENV HOME=/home/user

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    sudo git zip unzip openjdk-17-jdk \
    python3-pip python3-dev python3-venv \
    autoconf libtool pkg-config zlib1g-dev libncurses-dev \
    cmake libffi-dev libssl-dev automake \
    libsdl2-dev libsdl2-ttf-dev libsdl2-mixer-dev libsdl2-image-dev \
    make build-essential wget curl \
    && rm -rf /var/lib/apt/lists/*

# Создаём пользователя
RUN useradd -m -s /bin/bash user && echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Переключаемся на пользователя
USER user
WORKDIR /home/user

# Устанавливаем Python 3.11.16 через deadsnakes PPA
RUN sudo apt-get update && \
    sudo apt-get install -y software-properties-common && \
    sudo add-apt-repository -y ppa:deadsnakes/ppa && \
    sudo apt-get update && \
    sudo apt-get install -y python3.11 python3.11-dev python3.11-venv && \
    sudo rm -rf /var/lib/apt/lists/*

# Создаём виртуальное окружение с Python 3.11
RUN python3.11 -m venv /home/user/venv

# Активируем виртуальное окружение и устанавливаем Buildozer
ENV PATH="/home/user/venv/bin:$PATH"
RUN pip install --upgrade pip && \
    pip install buildozer cython

# Проверяем версию Python
RUN python --version

# Создаём папку для кэша Buildozer
RUN mkdir -p /home/user/.buildozer

# Рабочая директория
WORKDIR /home/user/build

CMD ["bash"]
