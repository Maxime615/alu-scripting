#!/usr/bin/python3
"""
A recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords.
"""

import re
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries Reddit API and counts
    keyword occurrences in hot posts.
    """
    if counts is None:
        counts = {}
        for word in word_list:
            w = word.lower()
            counts[w] = counts.get(w, 0)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my-script/0.1"}
    params = {"after": after, "limit": 100}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    try:
        data = response.json().get("data", {})
        children = data.get("children", [])
        after = data.get("after")

        for child in children:
            title = child.get("data", {}).get("title", "").lower()
            for word in counts.keys():
                matches = re.findall(
                    r'\b{}\b'.format(re.escape(word)),
                    title
                )
                counts[word] += len(matches)

        if after is not None:
            return count_words(subreddit, word_list, after, counts)
        else:
            filtered = {k: v for k, v in counts.items() if v > 0}
            if not filtered:
                return

            sorted_words = sorted(
                filtered.items(),
                key=lambda item: (-item[1], item[0])
            )

            for word, count in sorted_words:
                print("{}: {}".format(word, count))

    except ValueError:
        return
