#!/usr/bin/python3
"""Return list of all hot articles recursively to get all the results(not limited by pagination)."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetch all hot post titles append them in a list and then return the list."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "script:com.subscribers-count.myredditapp:v1.0 (by /u/yonasdejene)"}
    params = {"after": after, "limit": 100}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    posts = data.get("children", [])

    if not posts:
        return hot_list # empty list by default

    for post in posts:
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after") # None by default
    if after:
        return recurse(subreddit, hot_list, after) # recurssion if we find a value for after other than the default None
    return hot_list
