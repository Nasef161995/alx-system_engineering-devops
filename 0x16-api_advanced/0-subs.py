#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    "function queries the Reddit API and returns the number of subscribers"
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0