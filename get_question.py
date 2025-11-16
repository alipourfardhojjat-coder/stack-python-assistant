# get_question.py
import random

questions = [
    "How to reverse a list in Python?",
    "What is the difference between list and tuple?",
    "How to handle exceptions properly?"
]

answer = "Here is a brief answer/explanation for the question."

question = random.choice(questions)

# خروجی را داخل فایل محلی runner
with open("/tmp/daily_question.txt", "w") as f:
    f.write(f"Question: {question}\nAnswer: {answer}")
