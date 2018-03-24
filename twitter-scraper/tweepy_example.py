import tweepy
from connection_helper import initialize_api

api = initialize_api()

stanford_tweets = api.user_timeline('stanford')
for tweet in stanford_tweets:
    print( tweet.created_at, tweet.text)
