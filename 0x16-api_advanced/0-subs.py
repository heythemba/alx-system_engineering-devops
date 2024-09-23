import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit. If the subreddit is invalid, returns 0.
    """
    # Set up the URL for the subreddit's 'about' page in the API
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Reddit requires a custom User-Agent
    headers = {'User-Agent': 'python:subreddit.subscriber.count:v1.0 (by /u/yourusername)'}
    
    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the number of subscribers
            return data['data']['subscribers']
        else:
            # If the status code isn't 200, return 0
            return 0
    except Exception as e:
        # In case of any errors (e.g., connection issues), return 0
        return 0
