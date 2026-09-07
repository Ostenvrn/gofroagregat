FROM ubuntu:22.04

# Устанавливаем переменные окружения
ENV DEBIAN_FRONTEND=noninteractive
ENV USER=user
ENV HOME=/home/user

# ============================================================
# ШАГ 1: Обновляем репозитории и устанавливаем базовые зависимости
# ============================================================
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
    make \
    build-essential \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    liblzma-dev \
    && rm -rf /var/lib/apt/lists/*

# ============================================================
# ШАГ 2: Создаём пользователя
# ============================================================
RUN useradd -m -s /bin/bash user && echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# ============================================================
# ШАГ 3: Переключаемся на пользователя
# ============================================================
USER user
WORKDIR /home/user

# ============================================================
# ШАГ 4: Устанавливаем pyenv
# ============================================================
RUN curl https://pyenv.run | bash

# Добавляем pyenv в PATH
ENV PYENV_ROOT="$HOME/.pyenv"
ENV PATH="$PYENV_ROOT/bin:$PATH"

# ============================================================
# ШАГ 5: Устанавливаем Python 3.11.16 через pyenv
# ============================================================
RUN eval "$(pyenv init --path)" && \
    pyenv install 3.11.16 && \
    pyenv global 3.11.16

# ============================================================
# ШАГ 6: Устанавливаем pip и Buildozer
# ============================================================
RUN eval "$(pyenv init --path)" && \
    pip install --upgrade pip && \
    pip install buildozer cython

# ============================================================
# ШАГ 7: Проверяем версию Python
# ============================================================
RUN eval "$(pyenv init --path)" && python --version

# ============================================================
# ШАГ 8: Создаём папку для кэша Buildozer
# ============================================================
RUN mkdir -p /home/user/.buildozer/cache && \
    chown -R user:user /home/user/.buildozer
RUN mkdir -p /home/user/.buildozer

# ============================================================
# ШАГ 9: Рабочая директория
# ============================================================
WORKDIR /home/user/build

# Команда по умолчанию
CMD ["bash"]
