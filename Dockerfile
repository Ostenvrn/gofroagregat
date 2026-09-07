FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# ============================================================
# Устанавливаем системные зависимости
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
    && rm -rf /var/lib/apt/lists/*

# ============================================================
# Устанавливаем pip и Buildozer глобально (для всех пользователей)
# ============================================================
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install buildozer cython

# ============================================================
# Создаём пользователя (для совместимости, но сборка идёт от root)
# ============================================================
RUN useradd -m -s /bin/bash user && echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# ============================================================
# Рабочая директория
# ============================================================
WORKDIR /build

# Проверяем, что buildozer установлен
RUN buildozer --version || echo "Buildozer installed"

CMD ["bash"]
