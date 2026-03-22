import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_post(post):
    prompt = f"""
You are classifying Reddit posts for a product team.

Choose exactly one category from this list only:
Bug
Feature Request
Complaint
Praise
Question
Trend

Rules:
- Return only the category name
- Do not return any explanation
- If the post describes broken functionality, errors, misleading notifications, or something not working as intended, classify it as Bug

Post title: {post['title']}
Post text: {post['text']}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()