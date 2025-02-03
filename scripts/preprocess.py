import os
import re
import json

# تابع برای تمیز کردن متن و استخراج فقط کلمات
def clean_text(text):
    # حذف لینک‌ها
    text = re.sub(r'http\S+', '', text)
    # حذف تاریخ‌ها (هجری، شمسی، میلادی)
    text = re.sub(r'\d{4}[قش]|\d{1,2} [آ-ی]{3,9} \d{4}[مقش]|[\d]+', '', text)
    # حذف علائم نگارشی و کاراکترهای خاص
    text = re.sub(r'[^\w\s\u0600-\u06FF]', ' ', text)  # فقط کاراکترهای فارسی و فاصله نگه داشته شود
    # حذف خطوط اضافی و کلمات تکراری مانند رده‌ها، زبان‌ها و سایر عبارات زائد
    text = re.sub(r'زبان‌ها.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'رده‌ها.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'مشاهدۀ تاریخچۀ ویرایش.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'این صفحه آخرین‌بار.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'برگرفته از.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'(\s+\w{1,2}\s+)', ' ', text)  # حذف کلمات بسیار کوتاه (یک یا دو حرفی)
    # حذف فاصله‌های اضافی
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

# پیش‌پردازش مقاله
def preprocess_article(article_text):
    # تمیز کردن متن
    article_text = clean_text(article_text)
    # تبدیل حروف به کوچک (نرمال‌سازی)
    article_text = article_text.lower()
    return article_text

# تابع برای پردازش تمام مقالات
def process_articles(data_folder, output_file):
    articles_data = []
    
    # خواندن تمام فایل‌ها از پوشه data
    for filename in os.listdir(data_folder):
        if filename.endswith(".txt"):  # فقط فایل‌های متنی پردازش شوند
            with open(os.path.join(data_folder, filename), 'r', encoding='utf-8') as f:
                article_text = f.read()  # خواندن متن مقاله
                preprocessed_text = preprocess_article(article_text)  # پیش‌پردازش
                
                # ذخیره داده‌ها
                article_data = {
                    "cleaned_text": preprocessed_text  # مقاله پیش‌پردازش‌شده
                }
                articles_data.append(article_data)
    
    # ذخیره داده‌ها به فایل JSONL
    with open(output_file, 'w', encoding='utf-8') as f:
        for article in articles_data:
            json.dump(article, f, ensure_ascii=False)
            f.write("\n")

# مسیرهای فایل
data_folder = r"D:\QuestionCorpusProject\data"  # مسیر پوشه مقالات خام
output_file = r"D:\QuestionCorpusProject\output\articles_cleaned.jsonl"  # فایل خروجی

# پردازش مقالات
process_articles(data_folder, output_file)
