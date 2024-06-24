import tweepy
import time
import configparser

# Read configuration from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

API_KEY = config['TwitterAPI']['API_KEY']
API_SECRET_KEY = config['TwitterAPI']['API_SECRET_KEY']
ACCESS_TOKEN = config['TwitterAPI']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['TwitterAPI']['ACCESS_TOKEN_SECRET']

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Keywords to search for
keywords = ['keyword1', 'keyword2', 'keyword3']

# Responses based on keywords
responses = {
    'keyword1': 'Response to keyword1',
    'keyword2': 'Response to keyword2',
    'keyword3': 'Response to keyword3'
}

# Function to search and reply to tweets
def search_and_reply():
    for keyword in keywords:
        print(f"Searching for tweets containing: {keyword}")
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(10):
            try:
                tweet_id = tweet.id
                username = tweet.user.screen_name
                reply_text = f"@{username} {responses[keyword]}"
                
                # Avoid replying to yourself
                if username != api.me().screen_name:
                    api.update_status(status=reply_text, in_reply_to_status_id=tweet_id)
                    print(f"Replied to @{username}: {reply_text}")
                    time.sleep(15)  # Delay to avoid hitting rate limit
                else:
                    print("Skipped replying to own tweet")
                    
            except tweepy.TweepError as e:
                print(f"Error: {e.reason}")
            except StopIteration:
                break

# Run the function every 10 minutes
while True:
    search_and_reply()
    time.sleep(600)
