import tweepy
import configparser

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# Access the Twitter API credentials
api_key = 'uF4TG3vKanw346tx9PkohXFa2'
api_key_secret = 'CmTCfEQ8faAL5M68qQVGibgTr9yHDYdIuMhq1Vk32rfmB48EoV'
access_token ='1247067426-D5GQHtJlDIbFGqfh8EQqHDbfn6kPygy5toW4f1j'
access_token_secret = 'YvG8D4yJf7nU50DiNZ5IRUEtbEd8hkwJKBB62sAf5RiZk'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)

# Verify credentials
try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print(f"Error during authentication: {e}")

# Read the list of accounts from the file
with open('C:\\Users\\Kevin\\Pictures\\goon\\goon\\accounts.txt', 'r') as file:
    accounts = file.readlines()

# Follow each account in the list
for account in accounts:
    account = account.strip()
    if account:
        try:
            api.create_friendship(screen_name=account)
            print(f"Successfully followed: {account}")
        except tweepy.errors.Forbidden as e:
            print(f"Error following {account}: Forbidden - {e.response.json()['errors'][0]['message']}")
        except tweepy.errors.TweepyException as e:
            print(f"Error following {account}: {e}")

print("Finished following all accounts.")