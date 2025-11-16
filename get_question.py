import random

# نمونه متن تستی؛ بعداً این را با StackOverflow API جایگزین کن
questions = [
    "How to reverse a list in Python?",
    "What is the difference between list and tuple?",
    "How to handle exceptions properly?"
]

answer = "Here is a brief answer/explanation for the question."

# انتخاب تصادفی یک سوال
question = random.choice(questions)

# چاپ خروجی به صورت قابل خواندن
print("===DAILY_QUESTION_START===")
print(f"Question: {question}")
print(f"Answer: {answer}")
print("===DAILY_QUESTION_END===")

