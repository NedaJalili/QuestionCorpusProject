import json

# مسیر ورودی و خروجی
input_file = "output/articles_cleaned.jsonl"
output_file = "output/formatted_articles.jsonl"

# خواندن و پردازش فایل
with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
    for line in infile:
        data = json.loads(line.strip())  # تبدیل خط به دیکشنری
        formatted_data = {"raw_test": data.get("cleaned_text", "")}  # ذخیره متن در کلید raw_test
        outfile.write(json.dumps(formatted_data, ensure_ascii=False) + "\n")  # ذخیره در فایل جدید

print(f"فایل جدید در {output_file} ذخیره شد.")
