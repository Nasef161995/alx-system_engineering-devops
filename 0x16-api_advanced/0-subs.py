#!/usr/bin/python3
"""function queries the Reddit API"""
import requests
import re

def number_of_subscribers(subreddit):
    """function queries the Reddit API and returns the number of subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about/"
    res = requests.get(url)
    html = res.text
    pattern = r'subscribers="([^"]*)"'
    subscribers = re.search(pattern, html)

    if subscribers:
        return int(subscribers[0][13:-1])
    else:
        return 0
