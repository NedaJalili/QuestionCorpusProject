import json
import random
import re

def load_articles(input_file):
    """خواندن فایل JSONL ورودی و بارگذاری مقالات."""
    articles = []
    with open(input_file, "r", encoding="utf-8") as infile:
        for line in infile:
            article_data = json.loads(line)
            articles.append(article_data)
    return articles

def preprocess_text(text):
    """پیش‌پردازش متن برای نرمال‌سازی (حذف علائم و موارد غیر ضروری)."""
    # حذف علائم نگارشی
    text = re.sub(r'[^\w\s]', '', text)
    # تبدیل به حروف کوچک
    text = text.lower()
    # حذف فضاهای اضافی
    text = " ".join(text.split())
    return text

def extract_key_information(article_text):
    """استخراج اطلاعات کلیدی مانند تاریخ‌ها و نام‌ها از مقاله."""
    sentences = article_text.split(". ")
    key_info = {
        "dates": [re.findall(r"\d{4}", sentence) for sentence in sentences],
        "names": [re.findall(r"\b[A-Z][a-z]*\b", sentence) for sentence in sentences],
    }
    return key_info

def generate_questions(article_text):
    """تولید 20 سوال و جواب از مقاله."""
    questions = []
    key_info = extract_key_information(article_text)
    
    for i in range(1, 21):
        question = ""
        answer = ""
        
        # سوالات بر اساس تاریخ‌ها
        if key_info["dates"]:
            question = f"چه تاریخی در مقاله ذکر شده است؟"
            # اطمینان از این که لیست خالی نیست
            date_choices = [date for sublist in key_info["dates"] for date in sublist if date]
            if date_choices:
                answer = random.choice(date_choices)
        
        # سوالات بر اساس نام‌ها
        if not answer and key_info["names"]:
            question = f"چه نام‌هایی در مقاله ذکر شده‌اند؟"
            # اطمینان از این که لیست خالی نیست
            name_choices = [name for sublist in key_info["names"] for name in sublist if name]
            if name_choices:
                answer = random.choice(name_choices)
        
        # سوالات عمومی (در صورتی که تاریخ یا نامی پیدا نشد)
        if not question or not answer:
            question = f"سوال {i} چیست؟"
            answer = f"پاسخ {i}"
        
        questions.append((question, answer))
    
    return questions

def save_to_jsonl(output_file, data_list):
    """ذخیره داده‌ها در فایل JSONL."""
    with open(output_file, "w", encoding="utf-8") as outfile:
        for data in data_list:
            outfile.write(json.dumps(data, ensure_ascii=False) + "\n")
    print(f"داده‌ها با موفقیت در {output_file} ذخیره شدند.")

def process_articles(input_file, output_file):
    """پردازش مقالات و ذخیره خروجی به فرمت جدید."""
    articles = load_articles(input_file)
    output_data = []
    
    for article in articles:
        raw_text = article.get("raw_test", "")
        # پیش‌پردازش متن
        raw_text_prp = preprocess_text(raw_text)
        # تولید سوالات
        questions = generate_questions(raw_text)
        
        # ساخت دیکشنری نهایی برای هر مقاله
        formatted_data = {"raw_test": raw_text, "raw_test_prp": raw_text_prp}
        for idx, (q, a) in enumerate(questions, start=1):
            formatted_data[f"question{idx}"] = q
            formatted_data[f"answer{idx}"] = a
        
        output_data.append(formatted_data)
    
    # ذخیره خروجی در فایل
    save_to_jsonl(output_file, output_data)

if __name__ == "__main__":
    input_path = "output/formatted_articles.jsonl"  # مسیر فایل ورودی
    output_path = "output/final_dataset.jsonl"      # مسیر فایل خروجی
    process_articles(input_path, output_path)
