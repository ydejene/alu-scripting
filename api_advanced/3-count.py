#!/usr/bin/python3
"""Count keyword occurrences in hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Recursively count keywords in subreddit hot titles."""
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "script:com.subscribers-count.myredditapp:v1.0 (by /u/yonasdejene)"}
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})
    posts = data.get("children", [])

    for post in posts:
        title = post.get("data", {}).get("title", "").lower().split()
        for word in word_list:
            counts[word.lower()] += title.count(word.lower())

    after = data.get("after")
    if after:
        return count_words(subreddit, word_list, after, counts)

    sorted_counts = sorted(
        [(word, count) for word, count in counts.items() if count > 0],
        key=lambda x: (-x[1], x[0])
    )

    for word, count in sorted_counts:
        print(f"{word}: {count}")
a