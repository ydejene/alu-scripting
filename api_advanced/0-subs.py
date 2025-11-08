#!/usr/bin/python3
"""Get number of subscribers for a subreddit. If invalid return 0."""
import requests


def number_of_subscribers(subreddit):
    """Return total number of subscribers for a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "script:com.subscribers-count.myredditapp:v1.0 (by /u/yonasdejene)"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    return data.get("subscribers", 0)

