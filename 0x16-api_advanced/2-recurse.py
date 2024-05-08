#!/usr/bin/python3
'''
displays top 10 hot posts
'''
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
     queries the Reddit API and returns a list containing the
     titles of all hot articles for a given subreddit
     """
    user_agent = {'User-agent': 'Guantaiidah'}
    sub = requests.get('http://www.reddit.com/r/{}/hot.json?after={}'
                       .format(subreddit, after), headers=user_agent)

    try:
        sub = sub.json().get('data')
        after = sub.get('after')
        sub = sub.get('children')
        for obj in sub:
            hot_list.append(obj['data'].get('title'))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    except Exception as e:
        return None
