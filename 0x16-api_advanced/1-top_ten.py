#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("Error: Request failed with status code {}".format(response.status_code))
        return
    try:
        results = response.json().get("data")
        [print(c.get("data").get("title")) for c in results.get("children")]
    except ValueError:
        print("Error: Unable to parse JSON data")

if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    top_ten(subreddit)

