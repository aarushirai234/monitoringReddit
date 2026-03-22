import json
import os
import re
import streamlit as st
import pandas as pd

st.set_page_config(page_title="monitoringReddit", layout="wide")

REPORT_FILE = "report.txt"
POSTS_FILE = "posts.json"


def load_report():
    if os.path.exists(REPORT_FILE):
        with open(REPORT_FILE, "r", encoding="utf-8") as f:
            return f.read()
    return ""


def load_posts():
    if os.path.exists(POSTS_FILE):
        with open(POSTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def extract_section(report, possible_names):
    if isinstance(possible_names, str):
        possible_names = [possible_names]

    for name in possible_names:
        pattern = rf"##\s+.*?{re.escape(name)}(.*?)(?=\n## |\Z)"
        match = re.search(pattern, report, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()

    return ""


def count_category(posts, category_name):
    aliases = {
        "bug": {"bug", "bugs", "issue", "issues", "bugs & issues", "bugs / issues"},
        "feature request": {"feature request", "feature requests"},
        "complaint": {"complaint", "complaints"},
    }

    valid_labels = aliases.get(category_name.lower(), {category_name.lower()})

    return sum(
        1
        for p in posts
        if p.get("category", "").strip().lower() in valid_labels
    )


report = load_report()
posts = load_posts()

st.title("🔍 monitoringReddit")
st.caption(
    "AI agent to read Reddit data to generate product insights: "
    "🔥 top trends, 💬 user sentiment, 🐞 bugs, and ✅ recommended next steps."
)

if not report and not posts:
    st.warning("No output found yet. Run `python3 main.py` first.")
    st.stop()

# Top metrics
total_posts = len(posts)
bug_count = count_category(posts, "Bug")
feature_count = count_category(posts, "Feature Request")
complaint_count = count_category(posts, "Complaint")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Posts analyzed", total_posts)
m2.metric("Bug signals", bug_count)
m3.metric("Feature requests", feature_count)
m4.metric("Complaints", complaint_count)

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Insights Dashboard", "Recommended Actions", "Post Explorer", "Raw Report"]
)

with tab1:
    c1, c2 = st.columns(2)

    with c1:
        with st.container(border=True):
            st.subheader("🔥 Top Trends")
            section = extract_section(report, ["Top Trends", "Trends"])
            if section:
                st.markdown(section)
            else:
                st.info("No top trends section found.")

        with st.container(border=True):
            st.subheader("⚠️ Key Complaints")
            section = extract_section(report, ["Key Complaints", "Complaints"])
            if section:
                st.markdown(section)
            else:
                st.info("No key complaints section found.")

    with c2:
        with st.container(border=True):
            st.subheader("💬 Overall User Sentiment")
            section = extract_section(report, ["Overall Sentiment", "Sentiment"])
            if section:
                st.markdown(section)
            else:
                st.info("No overall sentiment section found.")

        with st.container(border=True):
            st.subheader("🐞 Bugs & Issues")
            section = extract_section(report, ["Bugs & Issues", "Bugs / Issues", "Bugs"])
            if section:
                st.markdown(section)
            else:
                st.info("No bugs section found.")

with tab2:
    st.subheader("✅ Recommended Actions")
    section = extract_section(
        report,
        ["Recommended Actions", "Recommended Next Steps", "Actions", "Next Steps"]
    )
    if section:
        st.markdown(section)
    else:
        st.info("No recommended actions section found.")

with tab3:
    st.subheader("Post Explorer")

    if posts:
        df = pd.DataFrame(posts)

        left, mid, right = st.columns(3)

        with left:
            if "category" in df.columns:
                category_options = ["All"] + sorted(df["category"].dropna().unique().tolist())
            else:
                category_options = ["All"]
            selected_category = st.selectbox("Category", category_options)

        with mid:
            if "subreddit" in df.columns:
                subreddit_options = ["All"] + sorted(df["subreddit"].dropna().unique().tolist())
            else:
                subreddit_options = ["All"]
            selected_subreddit = st.selectbox("Subreddit", subreddit_options)

        with right:
            min_score = st.slider("Minimum score", 0, 500, 20)

        filtered_df = df.copy()

        if selected_category != "All":
            filtered_df = filtered_df[filtered_df["category"] == selected_category]

        if selected_subreddit != "All":
            filtered_df = filtered_df[filtered_df["subreddit"] == selected_subreddit]

        if "score" in filtered_df.columns:
            filtered_df = filtered_df[filtered_df["score"] >= min_score]

        display_columns = ["title", "category", "subreddit", "score", "comments", "url"]
        available_columns = [col for col in display_columns if col in filtered_df.columns]

        st.dataframe(
            filtered_df[available_columns],
            use_container_width=True,
            height=350
        )

        st.markdown("### Selected Posts")
        for _, row in filtered_df.head(15).iterrows():
            with st.expander(row.get("title", "No title")):
                st.write(f"**Category:** {row.get('category', 'Unknown')}")
                st.write(f"**Subreddit:** {row.get('subreddit', 'Unknown')}")
                st.write(f"**Score:** {row.get('score', 0)}")
                st.write(f"**Comments:** {row.get('comments', 0)}")
                if row.get("text"):
                    st.write(row.get("text"))
                if row.get("url"):
                    st.markdown(f"[Open source post]({row.get('url')})")
    else:
        st.info("No posts found.")

with tab4:
    st.subheader("Raw Report")
    if report:
        st.markdown(report)
    else:
        st.info("No raw report found.")