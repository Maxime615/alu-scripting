#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Recursively queries Reddit API for all hot post titles of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my-script/0.1"}
    params = {"after": after, "count": count, "limit": 100}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
        after = data.get("after")

        for child in children:
            hot_list.append(child.get("data", {}).get("title"))

        if after is not None:
            return recurse(
                subreddit,
                hot_list=hot_list,
                after=after,
                count=count + len(children)
            )
        return hot_list
    except ValueError:
        return None
```[cite: 13]
