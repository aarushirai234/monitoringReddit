# 🔍 monitoringReddit - AI Agent

## ⚡ TL;DR
AI agent that scans Reddit to help product teams (e.g., Instagram) automatically detect user trends, bugs, sentiment shifts, and product opportunities—without manually reading posts.

## 🌐 Live Demo -
Click Here -> [https://monitoringreddit-aarushirai.streamlit.app/](url)


---

## 🎯 Problem

Product teams (e.g., Instagram) rely on external sources like Reddit to understand user sentiment, bugs, and feature requests. For platforms like Instagram, user feedback is often fragmented across communities, making it difficult to detect emerging issues early, identify consistent user pain points and synthesize insights into actionable decisions  

This process is manual, slow, and not scalable.

---

## 🚀 Solution

Built an AI-powered system that:

- Ingests real-time Reddit discussions  
- Filters high-signal posts using engagement heuristics  
- Classifies posts into product-relevant categories  
- Generates grounded insights with source attribution  
- Displays results via an interactive dashboard  

While this implementation focuses on Instagram-related subreddits, the system is modular and can be easily adapted to other products and platforms.

---

## 🖥️ Demo

### Insights Dashboard
![Insights](1.%20Insights%20Dashboard.png)

### Recommended Actions
![Actions](2.%20Recommended%20Actions.png)

### Post Explorer
![Explorer](3.%20Reddit%20Post%20Explorer.png)
## 🏗️ System Architecture

---

## 🧠 What it produces

- 🔥 Top user trends  
- ⚠️ Key complaints  
- 🐞 Emerging bugs  
- 💬 Overall user sentiment  
- ✅ Recommended product actions  

Each insight is backed by source Reddit posts.

---

Pipeline:

1. **Ingestion**
   - Fetches Reddit posts from Instagram-related subreddits (e.g., r/Instagram, r/socialmedia), configurable for other products  

2. **Filtering**
   - Filters posts based on engagement (score, comments)  

3. **Classification**
   - Categorizes posts into:
     - Bug  
     - Feature Request  
     - Complaint  
     - Trend  

4. **Summarization**
   - LLM generates grounded insights with supporting URLs  

5. **Visualization**
   - Streamlit dashboard for exploration and analysis  

---

## ⚙️ Tech Stack

- Python  
- OpenAI API  
- Streamlit  
- Requests  
- Pandas  

---

## ▶️ How to run

```bash
pip install -r requirements.txt
python main.py
streamlit run app.py
