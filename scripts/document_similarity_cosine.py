import json
import numpy as np
from scipy.sparse import load_npz
from sklearn.metrics.pairwise import cosine_similarity

# بارگذاری ماتریس ترم-داکیومنت
tdm_matrix = load_npz("D:/QuestionCorpusProject/output/tdm_matrix.npz")

# محاسبه مشابهت کسینوسی بین داکیومنت ۱ و ۴ داکیومنت دیگر
document_1 = tdm_matrix[0]  # داکیومنت 1
similarities = []

# مقایسه داکیومنت 1 با 4 داکیومنت دیگر
for i in range(1, 5):
    document_i = tdm_matrix[i]
    similarity = cosine_similarity(document_1, document_i)
    similarities.append({
        "document_1": 1,
        f"document_{i+1}": i+1,
        "similarity_score": similarity[0][0]
    })

# ذخیره نتایج در فایل خروجی
output_file = "output/document_similarities.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(similarities, f, ensure_ascii=False, indent=4)

print(f"نتایج مشابهت‌ها در فایل {output_file} ذخیره شد.")
