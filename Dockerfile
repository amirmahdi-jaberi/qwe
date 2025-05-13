FROM python:3.11-slim

# نصب وابستگی‌های موردنیاز برای اجرای Chrome در داکر
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \
    curl \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libgbm1 \
    libvulkan1 \
    xdg-utils \
    ca-certificates \
    xvfb \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# نصب مرورگر کروم
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# نصب Chromedriver هماهنگ با نسخه‌ی Chrome
ENV CHROME_DRIVER_VERSION=136.0.7103.92
RUN wget -q https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/$CHROME_DRIVER_VERSION/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf chromedriver-linux64* chromedriver-linux64.zip

RUN cp /usr/local/bin/chromedriver /usr/bin/
RUN echo "نسخه نصب شده chromedriver:" && chromedriver --version

# تعیین محل پروژه
WORKDIR /app
COPY . /app

# نصب پکیج‌های پایتون
RUN pip install --no-cache-dir -r requirements.txt

# اضافه کردن متغیر محیطی برای جلوگیری از کرش Chrome
ENV CHROME_HEADLESS="--headless=new --no-sandbox --disable-dev-shm-usage"

# اجرای برنامه
CMD ["python", "main.py"]
