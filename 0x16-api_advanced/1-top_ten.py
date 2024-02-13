#!/usr/bin/python3
"""function that queries the Reddit API"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    # Provide a descriptive User-Agent header
    headers = {"User-Agent": "My Reddit API Client"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]

        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print("None")
