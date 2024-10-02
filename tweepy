# Importing Tweepy
import tweepy

# Credentials
api_key = "INSERT API KEY"
api_secret = "INSERT API KEY SECRET"
bearer_token = r"INSERT BEARER TOKEN"
access_token = "INSERT ACCESS TOKEN"
access_token_secret = "INSERT ACCESS TOKEN SECRET"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


# Tweeting
client.create_tweet(text="Hello World")
