#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first 10 hot posts.
    If the subreddit is invalid, it prints None.
    """
    
    # Make an HTTP GET request to the Reddit API's "hot" endpoint, limiting to first 10 posts.
    api = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"limit": 10},
    )

    # Check the HTTP response status code.
    if api.status_code == 200:
        # If the status code is 200, print the titles of first 10 hot posts in JSON
        for post_data in api.json().get("data").get("children"):
            post = post_data.get("data")
            title = post.get("title")
            print(title)
    else:
        # If the status code is not 200, print None.
        print(None)
