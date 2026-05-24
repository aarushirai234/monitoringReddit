# Reddit Insight Agent 🔎

An AI workflow that turns Reddit conversations into PM-ready product insights with source attribution.

Part of **AI Product OS** — my open-source toolkit of AI workflows for product teams.

## 📌 TL;DR

Reddit Insight Agent scans Reddit to help product teams automatically detect user trends, bugs, sentiment shifts, and product opportunities without manually reading hundreds of posts.

The current implementation focuses on Instagram-related conversations, but the workflow can be adapted to other products, communities, and external feedback sources.

## 🌐 Live Demo

[Open the Streamlit demo](https://monitoringreddit-aarushirai.streamlit.app/)

---

## 🎯 Problem

Product teams often rely on external sources like Reddit, forums, app reviews, and social conversations to understand user sentiment, bugs, and feature requests.

For large consumer products like Instagram, useful feedback is fragmented across communities. This makes it hard to:

- detect emerging issues early
- identify repeated user pain points
- understand sentiment shifts
- separate noise from high-signal feedback
- synthesize messy conversations into product decisions

This process is usually manual, slow, and not scalable.

---

## 🚀 Solution

Reddit Insight Agent is an AI-powered workflow that:

- ingests Reddit discussions from product-relevant communities
- filters high-signal posts using engagement heuristics
- classifies posts into product-relevant categories
- generates source-grounded insights
- recommends possible PM actions
- displays results in an interactive Streamlit dashboard

The goal is to reduce time-to-insight from hours of manual reading to minutes of structured analysis.

---

## 🖥️ Demo

### Insights Dashboard

![Insights](1.%20Insights%20Dashboard.png)

### Recommended Actions

![Actions](2.%20Recommended%20Actions.png)

### Reddit Post Explorer

![Explorer](3.%20Reddit%20Post%20Explorer.png)

---

## 🧠 What it produces

- 🔥 Top user trends
- ⚠️ Key complaints
- 🐞 Emerging bugs
- 💬 Overall user sentiment
- ✅ Recommended product actions
- 🔗 Source-backed evidence

Each insight is linked back to the Reddit posts that support it.

---

## 🏗️ System Architecture

```text
Reddit posts/comments
        ↓
Ingestion
        ↓
Engagement-based filtering
        ↓
Classification
        ↓
LLM summarization
        ↓
Source-grounded insights
        ↓
Streamlit dashboard
