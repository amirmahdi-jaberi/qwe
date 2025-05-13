from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
import os
import shutil
import time
from urllib3.exceptions import MaxRetryError

def scrape_excoino():
    # تعریف اولیه متغیرها
    driver = None
    temp_dir = None
    
    try:
        # تنظیمات Chrome برای سرور
        options = Options()
        
        # گزینه‌های ضروری برای سرور
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--remote-debugging-port=9222')
        
        # ایجاد پروفایل موقت منحصربفرد
        temp_dir = tempfile.mkdtemp()
        options.add_argument(f"--user-data-dir={temp_dir}")
        
        # تنظیم مسیر اجرایی chromium
        options.binary_location = '/usr/bin/chromium-browser'
        
        # استفاده از chromedriver سیستم
        service = Service(executable_path='/usr/bin/chromedriver')
        
        # راه‌اندازی درایور
        driver = webdriver.Chrome(service=service, options=options)
        
        # تنظیمات اضافی
        driver.set_window_size(1280, 1024)
        driver.implicitly_wait(10)
        
        # عملیات اسکرپینگ
        driver.get("https://www.excoino.com/market/exchange/xrp_irr")
        time.sleep(3)
        
        # پردازش داده‌ها
        result = {}
        # ... کد پردازش شما ...
        
        return result
        
    except MaxRetryError as e:
        print(f"خطای اتصال: {str(e)}")
        return None
    except Exception as e:
        print(f"خطای غیرمنتظره: {str(e)}")
        return None
    finally:
        # تمیزکاری منابع
        try:
            if driver is not None:
                driver.quit()
        except:
            pass
            
        try:
            if temp_dir is not None and os.path.exists(temp_dir):
                shutil.rmtree(temp_dir, ignore_errors=True)
        except:
            pass

if __name__ == "__main__":
    data = scrape_excoino()
    if data:
        print("عملیات موفقیت‌آمیز بود")
        print(data)
    else:
        print("خطا در انجام عملیات")