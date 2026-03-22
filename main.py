import json
from agents.ingest import fetch_reddit_posts
import agents.filter as filter_module
from agents.classify import classify_post
from agents.summarize import summarize_posts

def main():
    print("Fetching Reddit posts...")
    posts = fetch_reddit_posts()
    print(f"Fetched {len(posts)} posts")

    print("Filtering posts...")
    filtered_posts = filter_module.filter_posts(posts)
    print(f"Kept {len(filtered_posts)} posts after filtering")

    print("Classifying posts...")
    for post in filtered_posts:
        post["category"] = classify_post(post)

    print("Generating summary report...")
    report = summarize_posts(filtered_posts)

    print("\n===== WEEKLY REPORT =====\n")
    print(report)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    with open("posts.json", "w", encoding="utf-8") as f:
        json.dump(filtered_posts, f, ensure_ascii=False, indent=2)

    print("\nSaved report to report.txt")
    print("Saved structured posts to posts.json")

if __name__ == "__main__":
    main()