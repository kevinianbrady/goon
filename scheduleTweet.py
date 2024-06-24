from requests_oauthlib import OAuth1Session
import configparser
import json  # Import json module to handle JSON data
import random
import schedule
import time
from datetime import datetime, timedelta


# Read configuration from config.ini file
config = configparser.ConfigParser()
config.read('config.ini')

consumer_key = config['TwitterAPI']['API_KEY']
consumer_secret = config['TwitterAPI']['API_SECRET_KEY']
access_token = config['TwitterAPI'].get('ACCESS_TOKEN')
access_token_secret = config['TwitterAPI'].get('ACCESS_TOKEN_SECRET')

# OAuth1Session instance
oauth = OAuth1Session(consumer_key, client_secret=consumer_secret,
                      resource_owner_key=access_token,
                      resource_owner_secret=access_token_secret)

# List of tweets
tweets = [
    "🚀 Ready for the next big thing in crypto? $GOON is set to make waves on the #PolygonChain! Join us and ride the meme coin revolution! 👿 #GOONtoTheMoon",
    "👿 GOON MORNING! Start your day with the hottest meme coin on Polygon. $GOON is here to take over the crypto world! #MemeToken #Polygon #GOON 👿",
    "👿 GOON EVENING! As the day winds down, $GOON is just getting started. Join the movement and be part of something big. #CryptoCommunity #GOON 👿",
    "👿 To the moon and beyond! $GOON is on a mission to dominate the meme coin market. Don't miss out on this rocket ride! #GOONtoTheMoon #Polygon 👿",
    "👿 $GOON is 100% community driven with a massive CULT behind it. Be part of the revolution! Twitter: @Polygoon0x | TG: https://t.me/+Rq3sjm0bBDE3ZTdl #GOON 👿" ,
    "👿 $GOON: 1 Billion or Death! Join the movement and be part of the next big thing in crypto. #Polygon #MemeCoin" 👿,
    "👿 Polygon needs its native meme coin, and that's $GOON. Be part of the future of crypto. #GOON #PolygonChain" 👿,
]
#     "📈 $GOON is so undervalued it's not even funny. Get in now and ride the wave to the top! #GOON #CryptoGems #Polygon",
#     "💪 $GOON is the next big meme coin, built on Polygon with strong whale support and a passionate community. Don't miss out! #Crypto #GOONtoTheMoon",
#     "🔥 Not only is $GOON the premier meme coin on Polygon, it's also deflationary with 11% of its supply set to be burned at 1B MC! #LFGOON #Crypto",
#     "🚀 You missed Bitcoin, Ethereum, and Dogecoin... Don't miss out on $GOON! You're still early. #CryptoOpportunity #GOON",
#     "🛡️ 3 Bullish things about Polygon: top tech, growing users, and the best meme coin - $GOON. Join the revolution! #Crypto #PolygonChain",
#     "💎 1 Billy or Killy - $GOON is on its way to greatness. Be part of the journey! #GOONtoTheMoon #Polygon",
#     "🛡️ Don't get rug-pulled, invest in $GOON. Join our community on TG: http://t.me/PolyGOONs #SafeCrypto #GOON",
#     "💰 3 simple steps to get rich: Buy $GOON, Join $GOON TG: http://t.me/PolyGOONs, Spread the word. #CryptoSuccess #GOON",
#     "🦾 Is there a stronger narrative than 1B or Death? Join the $GOON army and be part of the movement! #CryptoCommunity #Polygon",
#     "📈 Guide on how NOT to lose all your money trading crypto: Buy $GOON, Hodl $GOON, Shill $GOON, Enjoy. #CryptoStrategy #GOON",
#     "💎 Personally, I would only buy $GOON on Polygon. It's the best bet on meme coins. #CryptoInvestment #PolygonChain",
#     "🔥 There are only 2 types of crypto portfolios: Those with $GOON (good ones) and those without (bad ones). Which one is yours? #Crypto #GOON",
#     "🚀 Next stop for $GOON is the moon! Join us on this exciting journey. #GOONtoTheMoon #MemeCoin #Polygon"
# ]


# Function to send a tweet
def send_tweet():
    tweet = random.choice(tweets)
    payload = {"text": tweet}  # Change to 'text' parameter for Twitter API v2
    url = "https://api.twitter.com/2/tweets"

    try:
        headers = {'Content-Type': 'application/json'}  # Specify Content-Type header
        response = oauth.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 201:
            print(f"Tweeted: {tweet}")
        else:
            print(f"Error posting tweet: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

# Schedule tweets at specific times
schedule.every().day.at("22:58").do(send_tweet)
schedule.every().day.at("13:10").do(send_tweet)
schedule.every().day.at("13:30").do(send_tweet)
schedule.every().day.at("13:50").do(send_tweet)
# Add more scheduled times as needed


# Function to schedule tweets at random times
# def schedule_random_tweets(num_tweets=10):
#     # Generate random times for tweeting
#     now = datetime.now()
#     tweet_times = []
    
#     for _ in range(num_tweets):
#         random_seconds = random.randint(0, 86400)  # Random number of seconds in a day
#         tweet_time = now + timedelta(seconds=random_seconds)
#         tweet_times.append(tweet_time.time())
    
#     # Schedule tweets at generated times
#     for tweet_time in tweet_times:
#         schedule_time = tweet_time.strftime("%H:%M:%S")
#         schedule.every().day.at(schedule_time).do(send_tweet)
#         print(f"Scheduled tweet at {schedule_time}")


# # Schedule random tweets
# schedule_random_tweets(num_tweets=7)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
