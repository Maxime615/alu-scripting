#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries Reddit API for all hot post titles."""
    headers = {"User-Agent": "linux:ah.reddit.task:v1.0 (by /u/winermancer)"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"after": after}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None

    try:
        results = response.json().get("data", {})
        after = results.get("after")
        children = results.get("children", [])
        for child in children:
            hot_list.append(child.get("data", {}).get("title"))

        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except ValueError:
        return None
