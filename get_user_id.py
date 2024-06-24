import requests
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')



# Access the Twitter API credentials
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAFKmuQEAAAAAqxnlArc%2B1IRgNOSjwE%2Br%2FKjxdE4%3DAhKWKRjkR45S4QwT1bUjC4t0B2lYGCU1d5bcE4VRXNJhZ1RZ57'


username = 'kevinianbrady'  # Replace with your Twitter handle

# Define the endpoint and headers
url = f"https://api.twitter.com/2/users/by/username/{username}"
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

# Make the request to get the user ID
response = requests.get(url, headers=headers)
if response.status_code == 200:
    user_data = response.json()
    user_id = user_data["data"]["id"]
    print(f"Your user ID is: {user_id}")
else:
    print(f"Error fetching user ID: {response.json()}")
