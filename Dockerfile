FROM ubuntu:22.04

# Устанавливаем переменные окружения
ENV DEBIAN_FRONTEND=noninteractive
ENV USER=user
ENV HOME=/home/user

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    sudo \
    git \
    zip \
    unzip \
    openjdk-17-jdk \
    python3-pip \
    python3-dev \
    autoconf \
    libtool \
    pkg-config \
    zlib1g-dev \
    libncurses-dev \
    cmake \
    libffi-dev \
    libssl-dev \
    automake \
    libsdl2-dev \
    libsdl2-ttf-dev \
    libsdl2-mixer-dev \
    libsdl2-image-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаём пользователя
RUN useradd -m -s /bin/bash user && echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Переключаемся на пользователя
USER user
WORKDIR /home/user

# Устанавливаем Python 3.11.16 через pyenv
RUN sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# Устанавливаем pyenv
RUN curl https://pyenv.run | bash

# Добавляем pyenv в PATH
ENV PYENV_ROOT="$HOME/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"

# Устанавливаем Python 3.11.16 через pyenv
RUN eval "$(pyenv init --path)" && \
    pyenv install 3.11.16 && \
    pyenv global 3.11.16

# Устанавливаем pip и Buildozer
RUN eval "$(pyenv init --path)" && \
    pip install --upgrade pip && \
    pip install buildozer cython

# Проверяем версию Python
RUN eval "$(pyenv init --path)" && python --version

# Создаём папку для кэша Buildozer
RUN mkdir -p /home/user/.buildozer

# Устанавливаем рабочую директорию
WORKDIR /home/user/build

# Команда по умолчанию
CMD ["bash"]
