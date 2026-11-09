#!/usr/bin/python3
"""
A function that queries the Reddit API and prints
the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Queries Reddit API for the first 10 hot posts of a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:holberton:top_ten:v1.0 (by /u/maxime)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json().get("data", {})
        posts = data.get("children", [])
        if not posts:
            print("None")
            return
        for post in posts:
            print(post.get("data", {}).get("title"))
    except ValueError:
        print("None")
