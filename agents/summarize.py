import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_posts(posts):
    combined_text = ""

    for i, p in enumerate(posts[:20]):
        combined_text += f"""
Post {i+1}:
Title: {p.get('title', '')}
Category: {p.get('category', 'Unknown')}
Subreddit: {p.get('subreddit', 'Unknown')}
Score: {p.get('score', 0)}
Comments: {p.get('comments', 0)}
URL: {p.get('url', '')}
Text: {p.get('text', '')}

"""

    prompt = f"""
You are a product insights analyst.

Analyze the Reddit posts and generate a clean, well-formatted report.

STRICT REQUIREMENTS:
- Use proper Markdown formatting with headers and bullet points
- Every insight must include 2-3 supporting post URLs
- Do not make claims without evidence
- Only use information from the provided posts
- If there is not enough evidence for a claim, do not include it
- Keep the report concise and readable
- Return exactly 3 items under Top Trends
- Return at most 3 items under Key Complaints
- Return at most 3 items under Bugs & Issues

FORMAT:

# Weekly Report: Reddit Product Insights

## Top Trends
### Trend 1
- Description
- **Supporting Posts:**
  - URL
  - URL

### Trend 2
- Description
- **Supporting Posts:**
  - URL
  - URL

### Trend 3
- Description
- **Supporting Posts:**
  - URL
  - URL

## Key Complaints
### Complaint 1
- Description
- **Supporting Posts:**
  - URL
  - URL

## Bugs & Issues
### Issue 1
- Description
- **Supporting Posts:**
  - URL
  - URL

## Overall Sentiment
- 2-3 concise sentences grounded in the posts

## Recommended Actions
- Action 1
  - **Supporting Posts:**
    - URL
    - URL

Posts:
{combined_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()