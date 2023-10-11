#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Query the api"""
    if subreddit is none or not isinstance(subreddit, str):
        return 0
    else:
        user_agent = {'User-agent': 'Google Chrome Version 117.0.5938.134 '}
        url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
        response = requests.get(url, headers=user_agent)
        data = response.json()

        return data.get('data').get('subscribers')




