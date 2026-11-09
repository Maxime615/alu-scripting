#!/usr/bin/python3
"""
A function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Queries Reddit API for the subscriber count of a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "my-script/0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except ValueError:
        return 0
