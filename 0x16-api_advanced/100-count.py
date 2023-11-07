#!/usr/bin/python3
"""Contains the count_words function"""
import requests

def count_words(subreddit, target_words, found_words=[], after_page=None):
    '''Prints counts of given words found in hot posts of a given subreddit.
    '''
    # Define the headers for the HTTP request.
    headers = {'User-agent': 'test45'}
    
    # Make an HTTP GET request to Reddit's API to fetch hot posts from the specified subreddit.
    hot_posts = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'.format(subreddit, after_page), headers=headers)
    
    # If 'after' is None, convert target_words to lowercase for case-insensitive matching.
    if after_page is None:
        target_words = [word.lower() for word in target_words]
    
    if hot_posts.status_code == 200:
        # Extract the data and 'after' value from the response.
        hot_posts_data = hot_posts.json()['data']
        after_page = hot_posts_data['after']
        hot_posts_data = hot_posts_data['children']
        
        # Iterate through the hot posts and search for target_words in the titles.
        for post in hot_posts_data:
            title = post['data']['title'].lower()
            for word in title.split(' '):
                if word in target_words:
                    found_words.append(word)
        
        if after_page is not None:
            # If 'after' is not None, continue to the next page of results.
            count_words(subreddit, target_words, found_words, after_page)
        else:
            # Calculate and print word counts.
            result = {}
            for word in found_words:
                if word.lower() in result:
                    result[word.lower()] += 1
                else:
                    result[word.lower()] = 1
            for key, value in sorted(result.items(), key=lambda item: item[1], reverse=True):
                print('{}: {}'.format(key, value))
    else:
        return
