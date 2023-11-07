#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

# Import the 'requests' library, which is used for making HTTP requests.
import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers for a subreddit.
    If the subreddit is invalid, it returns 0.
    """
    
    # Make an HTTP GET request to the Reddit API's "about" endpoint for the specified subreddit.
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    # Check the HTTP response status code.
    if req.status_code == 200:
        # If the status code is 200, get the number of subscribers in JSON.
        # Return the number of subscribers.
        return req.json().get("data").get("subscribers")
    else:
        # If the status code is not 200 (indicating an error or invalid subreddit), return 0.
        return 0
