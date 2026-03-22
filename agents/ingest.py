import requests

def fetch_reddit_posts():
    headers = {
        "User-Agent": "monitoringReddit/0.1"
    }

    subreddits = ["Instagram", "socialmedia", "InstagramMarketing"]
    posts = []

    for sub in subreddits:
        url = f"https://www.reddit.com/r/{sub}/top.json"
        params = {
            "t": "week",
            "limit": 25
        }

        response = requests.get(url, headers=headers, params=params, timeout=15)
        response.raise_for_status()

        payload = response.json()
        children = payload["data"]["children"]

        for child in children:
            post = child["data"]
            posts.append({
                "subreddit": sub,
                "title": post.get("title", ""),
                "text": post.get("selftext", ""),
                "score": post.get("score", 0),
                "comments": post.get("num_comments", 0),
                "url": f"https://www.reddit.com{post.get('permalink', '')}",
                "created_utc": post.get("created_utc")
            })

    return posts