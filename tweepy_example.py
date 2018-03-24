import tweepy

CONSUMER_KEY = "ZNLbPgqfFy7xzhvQXQBt2wYh9"
CONSUMER_SECRET = "uV6ZPfmESiLPdXxlOaIb6TXLOs388ARksI9mpQBoNOgNyQkesK"
ACCESS_TOKEN = "977546218413928453-iYPjjdsjp839ZH127QLOZXh8F2BAPRI"
ACCESS_TOKEN_SECRET = "g6I7eGGB2b8Ydivrn8DMuOrdmKQdwm7KFI8aidl7xT7nZ"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

stanford_tweets = api.user_timeline('stanford')
for tweet in stanford_tweets:
    print( tweet.created_at, tweet.text)
