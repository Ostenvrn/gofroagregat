FROM ubuntu:22.04

# ============================================================
# ОТКЛЮЧАЕМ ИНТЕРАКТИВНЫЕ ДИАЛОГИ (ВАЖНО!)
# ============================================================
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Moscow
ENV USER=user
ENV HOME=/home/user

# ============================================================
# УСТАНАВЛИВАЕМ СИСТЕМНЫЕ ЗАВИСИМОСТИ
# ============================================================
RUN apt-get update && apt-get install -y \
    sudo git zip unzip openjdk-17-jdk \
    python3-pip python3-dev python3-venv \
    autoconf libtool pkg-config zlib1g-dev libncurses-dev \
    cmake libffi-dev libssl-dev automake \
    libsdl2-dev libsdl2-ttf-dev libsdl2-mixer-dev libsdl2-image-dev \
    make build-essential wget curl \
    && rm -rf /var/lib/apt/lists/*

# ============================================================
# СОЗДАЁМ ПОЛЬЗОВАТЕЛЯ
# ============================================================
RUN useradd -m -s /bin/bash user && echo "user ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# ============================================================
# ПЕРЕКЛЮЧАЕМСЯ НА ПОЛЬЗОВАТЕЛЯ
# ============================================================
USER user
WORKDIR /home/user

# ============================================================
# УСТАНАВЛИВАЕМ PYTHON 3.11 ЧЕРЕЗ DEADSNAKES
# ============================================================
RUN sudo apt-get update && \
    sudo apt-get install -y software-properties-common && \
    sudo add-apt-repository -y ppa:deadsnakes/ppa && \
    sudo apt-get update && \
    sudo apt-get install -y python3.11 python3.11-dev python3.11-venv && \
    sudo rm -rf /var/lib/apt/lists/*

# ============================================================
# СОЗДАЁМ ВИРТУАЛЬНОЕ ОКРУЖЕНИЕ
# ============================================================
RUN python3.11 -m venv /home/user/venv

# ============================================================
# УСТАНАВЛИВАЕМ BUILD02ER
# ============================================================
ENV PATH="/home/user/venv/bin:$PATH"
RUN pip install --upgrade pip && \
    pip install buildozer cython

# ============================================================
# ПРОВЕРЯЕМ ВЕРСИЮ
# ============================================================
RUN python --version

# ============================================================
# ПАПКА ДЛЯ КЭША
# ============================================================
RUN mkdir -p /home/user/.buildozer

# ============================================================
# РАБОЧАЯ ДИРЕКТОРИЯ
# ============================================================
WORKDIR /home/user/build

CMD ["bash"]
