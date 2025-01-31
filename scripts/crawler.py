import os
import requests
from bs4 import BeautifulSoup
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import sys
sys.stdout.reconfigure(encoding='utf-8')

# پوشه ذخیره مقالات
DATA_DIR = "./data/"
os.makedirs(DATA_DIR, exist_ok=True)

# تنظیم ریتری برای مدیریت خطاهای اتصال
session = requests.Session()
retries = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))
session.mount('https://', HTTPAdapter(max_retries=retries))

def download_article(url, index):
    """
    دانلود مقاله از URL و ذخیره آن در پوشه مشخص‌شده.
    """
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # استخراج عنوان مقاله
        title_tag = soup.find('title')
        if not title_tag:
            print(f"عنوانی برای مقاله {url} یافت نشد.")
            return
        
        title = title_tag.get_text(strip=True).replace('/', '-')
        filename = f"{index}_{title[:50]}.txt"
        
        # ذخیره متن مقاله
        filepath = os.path.join(DATA_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(soup.get_text(strip=True))
        
        print(f"مقاله {index} با موفقیت ذخیره شد: {filename}")
    except Exception as e:
        print(f"خطا در دانلود مقاله {index}: {e}")

def scrape_articles(base_url, max_articles=5):
    """
    خزیدن وب‌سایت و دانلود حداکثر max_articles مقاله.
    """
    visited_links = set()
    queue = [base_url]
    article_count = 0

    while queue and article_count < max_articles:
        current_url = queue.pop(0)
        
        if current_url in visited_links:
            continue
        
        visited_links.add(current_url)
        try:
            response = session.get(current_url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # دانلود مقاله فعلی
            download_article(current_url, article_count + 1)
            article_count += 1
            
            # پیدا کردن لینک‌های جدید
            for link in soup.find_all('a', href=True):
                new_url = requests.compat.urljoin(current_url, link['href'])
                if new_url not in visited_links and base_url in new_url:
                    queue.append(new_url)
            
            # افزودن تأخیر بین درخواست‌ها
            time.sleep(2)
        except Exception as e:
            print(f"خطا در پردازش لینک {current_url}: {e}")

    print(f"تعداد کل مقالات دانلود شده: {article_count}")

if __name__ == "__main__":
    BASE_URL = "https://fa.wikishia.net"  # آدرس وبسایت هدف
    scrape_articles(BASE_URL, max_articles=5)
