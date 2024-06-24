import requests
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Access the Twitter API credentials
bearer_token = config['TwitterAPI']['BEARER_TOKEN']

# Define the endpoint and headers
url = "https://api.twitter.com/2/users/{}/following".format(your_user_id)
headers = {
    "Authorization": "Bearer {}".format(bearer_token),
    "Content-Type": "application/json"
}

# Read the list of accounts from the file
with open('accounts.txt', 'r') as file:
    accounts = file.readlines()

# Follow each account in the list
for account in accounts:
    account = account.strip()
    if account:
        # Get the user ID of the account to follow
        user_lookup_url = "https://api.twitter.com/2/users/by/username/{}".format(account)
        response = requests.get(user_lookup_url, headers=headers)
        if response.status_code == 200:
            user_id = response.json()["data"]["id"]
            follow_payload = {"target_user_id": user_id}
            response = requests.post(url, headers=headers, json=follow_payload)
            if response.status_code == 200:
                print(f"Successfully followed: {account}")
            else:
                print(f"Error following {account}: {response.json()}")
        else:
            print(f"Error finding {account}: {response.json()}")

print("Finished following all accounts.")
