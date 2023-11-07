#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""
import requests

def recurse(subreddit, hot_list=[], after=""):
    """
    Queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.

    - If not a valid subreddit, return None.
    """
    
    # Make an HTTP GET request to the Reddit API's "hot" endpoint
    # include the "after" parameter to get the next page of results.
    api = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
    )
    # Check the HTTP response status code.
    if api.status_code == 200:
        # If status code is 200, extract titles of the hot articles in JSON.
        for get_data in api.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)

        after = api.json().get("data").get("after")

        # If there is no "after" parameter, it means we've reached the last page of results, 
        # so return the hot_list.
        if after is None:
            return hot_list
        else:
            # Recursively call the function with the "after" parameter 
            # to fetch the next page of results.
            return recurse(subreddit, hot_list, after)
    else:
        # If the status code is not 200 return None.
        return None
