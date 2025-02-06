import json
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import scipy.sparse
import os

input_path = "output/formatted_articles.jsonl"  # مسیر فایل ورودی


# بررسی وجود فایل
if not os.path.exists(input_path):
    print(f"فایل {input_path} یافت نشد.")
else:
    # خواندن مقالات پردازش‌شده
    documents = []
    with open(input_path, "r", encoding="utf-8") as file:
        for line in file:
            data = json.loads(line)
            documents.append(data["raw_test"])  # دریافت متن مقاله

    # تبدیل متن‌ها به ماتریس ترم-داکیومنت با استفاده از TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000, stop_words=None)  # محدود کردن ویژگی‌ها به 5000 کلمه مهم
    X = vectorizer.fit_transform(documents)

    # ذخیره ماتریس به صورت فشرده برای استفاده‌های بعدی
    scipy.sparse.save_npz("output/tdm_matrix.npz", X)

    # ذخیره واژه‌ها (ویژگی‌های ماتریس) 
    with open("output/tdm_features.json", "w", encoding="utf-8") as f:
        json.dump(vectorizer.get_feature_names_out().tolist(), f, ensure_ascii=False)

    print("  ماتریس ترم-داکیومنت با موفقیت ساخته و ذخیره شد.")
    print("🔹 ابعاد ماتریس:", X.shape)  # (تعداد مقالات, تعداد ویژگی‌ها)
