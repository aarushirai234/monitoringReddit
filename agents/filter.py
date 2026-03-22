def filter_posts(posts, min_score=20, min_comments=5):
    filtered = []

    for post in posts:
        if post["score"] >= min_score and post["comments"] >= min_comments:
            filtered.append(post)

    return filtered