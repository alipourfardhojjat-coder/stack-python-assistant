import requests
import json

# ----------------------
# تنظیمات اولیه
# ----------------------
TAG = "python"  # زبان برنامه نویسی مورد نظر
PAGE_SIZE = 10  # تعداد سوالات بررسی شده در هر درخواست
UNANSWERED = True  # فقط سوالات بی جواب

# Stack Exchange API URL
API_URL = "https://api.stackexchange.com/2.3/questions"

# ----------------------
# گرفتن سوالات از API
# ----------------------
params = {
    "order": "desc",
    "sort": "creation",
    "tagged": TAG,
    "site": "stackoverflow",
    "pagesize": PAGE_SIZE,
    "filter": "!9_bDDxJY5"  # فیلتر شامل عنوان، لینک، body
}

response = requests.get(API_URL, params=params)
data = response.json()

# ----------------------
# فیلتر کردن سوالات بی جواب و با کیفیت
# ----------------------
questions = []
for item in data.get("items", []):
    if item.get("answer_count") == 0:
        # حذف سوالات کوتاه یا خیلی مبهم
        if len(item.get("title", "")) > 20:
            questions.append(item)

if not questions:
    print("No suitable unanswered Python questions found today.")
    exit()

# انتخاب فقط یک سوال (اولین مورد)
question = questions[0]

title = question.get("title")
link = question.get("link")
body = question.get("body_markdown", "")

# ----------------------
# آماده سازی متن برای AI و ارسال به تلگرام
# ----------------------
message = f"""
❓ سوال امروز:
{title}
Link: {link}

📝 توضیحات اولیه:
{body[:500]}...  # خلاصه متن سوال برای جلوگیری از طولانی شدن
"""

# ذخیره در فایل برای n8n یا AI
with open("daily_question.txt", "w", encoding="utf-8") as f:
    f.write(message)

print("Today's question prepared successfully!")
