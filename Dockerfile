FROM python:3

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1 \
    libglx-mesa0 \
    libgl1-mesa-dri \
    mesa-utils \
    libx11-6 \
    libxext6 \
    libxrender1 \
    libxrandr2 \
    libxinerama1 \
    libxi6 \
    libxcursor1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main_menu.py" ]