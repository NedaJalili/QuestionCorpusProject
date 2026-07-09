QuestionCorpusProject
معرفی پروژه
QuestionCorpusProject یک سیستم پردازش متن است که شامل مراحل مختلفی برای جمع‌آوری، پردازش و استخراج اطلاعات از مقالات می‌باشد. این پروژه با هدف تولید داده‌های ساختاریافته برای مدل‌های پردازش زبان طبیعی (NLP) و سیستم‌های پرسش و پاسخ طراحی شده است.
________________________________________
📁 ساختار پوشه‌های پروژه
data/
محتوا: مقالات خام دریافت‌شده از وب‌سایت
•	raw_articles.jsonl → مقالات اولیه بدون پردازش
output/
محتوا: خروجی‌های پردازش‌شده
•	articles_cleaned.jsonl → مقالات پیش‌پردازش‌شده
•	formatted_articles.jsonl → مقالات فرمت‌یافته در قالب دیکشنری
•	tdm_matrix.npz → ماتریس ترم-داکیومنت
•	tdm_features.json → ویژگی‌های استخراج‌شده (کلمات مهم)
•	document_similarities.json → شباهت‌های محاسبه‌شده بین مقالات
•	final_dataset.jsonl → مجموعه نهایی شامل سوالات و پاسخ‌ها
scripts/
محتوا: اسکریپت‌های پردازش متن
•	crawler.py → استخراج مقالات از وب‌سایت
•	preprocess.py → پیش‌پردازش متن (حذف نویزها و پاک‌سازی)
•	format_articles.py → فرمت‌دهی مقالات در قالب دیکشنری
•	build_tdm.py → ایجاد ماتریس ترم-داکیومنت
•	document_similarity_cosine.py → محاسبه شباهت کسینوسی مقالات
•	generate_questions.py → تولید سوال و جواب از مقالات
سایر فایل‌ها
•	crawler_errors.log → ثبت خطاهای اجرای crawler.py
•	README.md → توضیحات پروژه
________________________________________
🔹 مراحل پردازش داده‌ها
۱. استخراج مقالات
•	دریافت مقالات از وب‌سایت https://fa.wikishia.net با استفاده از crawler.py
•	ذخیره مقالات در پوشه data/
۲. پیش‌پردازش داده‌ها
•	حذف نویزها، علائم اضافی و پاک‌سازی متون با preprocess.py
•	ذخیره خروجی در output/articles_cleaned.jsonl
۳. فرمت‌دهی مقالات
•	تبدیل داده‌های پیش‌پردازش‌شده به قالب دیکشنری با format_articles.py
•	ذخیره خروجی در output/formatted_articles.jsonl
۴. ساخت ماتریس ترم-داکیومنت (TDM)
•	ایجاد ماتریس TF-IDF با build_tdm.py
•	ذخیره ماتریس در output/tdm_matrix.npz
•	ذخیره ویژگی‌های استخراج‌شده در output/tdm_features.json
۵. محاسبه شباهت مقالات
•	محاسبه فاصله کسینوسی بین مقالات با document_similarity_cosine.py
•	ذخیره خروجی در output/document_similarities.json
۶. تولید سوالات
•	تولید سوال و جواب از مقالات با generate_questions.py
•	ذخیره خروجی در output/final_dataset.jsonl
________________________________________
  کاربردها
•	تولید داده‌های آموزشی برای مدل‌های NLP
•	توسعه سیستم‌های پرسش و پاسخ
•	تحلیل شباهت متون و خوشه‌بندی مقالات
________________________________________
  نحوه مشارکت
اگر این پروژه برای شما مفید بود، لطفاً آن را ⭐ کنید. هرگونه پیشنهاد یا بهبود را می‌توانید از طریق Pull Request ارسال کنید.
✉️ ارتباط با من: neda.jalili.23@gmail.com
________________________________________
________________________________________
QuestionCorpusProject
Project Overview
QuestionCorpusProject is a text processing system designed to collect, process, and extract structured information from articles. The goal is to create structured datasets for NLP models and Q&A systems.
________________________________________
📁 Project Structure
data/
Content: Raw articles collected from the website
•	raw_articles.jsonl → Unprocessed articles
output/
Content: Processed data outputs
•	articles_cleaned.jsonl → Preprocessed articles
•	formatted_articles.jsonl → Articles formatted as dictionaries
•	tdm_matrix.npz → Term-document matrix
•	tdm_features.json → Extracted features (important words)
•	document_similarities.json → Computed article similarities
•	final_dataset.jsonl → Final dataset with generated Q&A pairs
scripts/
Content: Text processing scripts
•	crawler.py → Extract articles from the website
•	preprocess.py → Clean and preprocess text
•	format_articles.py → Convert articles into structured dictionaries
•	build_tdm.py → Generate term-document matrix
•	document_similarity_cosine.py → Compute cosine similarity between articles
•	generate_questions.py → Generate questions and answers from articles
Other Files
•	crawler_errors.log → Log file for crawler errors
•	README.md → Project documentation
________________________________________
🔹 Data Processing Steps
1. Article Extraction
•	Articles are scraped from https://fa.wikishia.net using crawler.py
•	Articles are stored in data/
2. Data Preprocessing
•	Noise removal, text cleaning using preprocess.py
•	Output stored in output/articles_cleaned.jsonl
3. Formatting Articles
•	Convert cleaned data into structured format using format_articles.py
•	Output stored in output/formatted_articles.jsonl
4. Building Term-Document Matrix (TDM)
•	Generate TF-IDF matrix using build_tdm.py
•	Matrix stored in output/tdm_matrix.npz
•	Extracted features stored in output/tdm_features.json
5. Computing Article Similarity
•	Compute cosine similarity between articles using document_similarity_cosine.py
•	Output stored in output/document_similarities.json
6. Generating Questions
•	Generate Q&A pairs using generate_questions.py
•	Output stored in output/final_dataset.jsonl
________________________________________
  Use Cases
•	Generating training data for NLP models
•	Developing Q&A systems
•	Text similarity analysis and article clustering
________________________________________
  Contributing
If you find this project useful, please ⭐ star it. Feel free to contribute by submitting a Pull Request.
✉️ Contact: neda.jalili.23@gmail.com
