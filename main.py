import tweepy
import time
import os

auth = tweepy.OAuthHandler(os.environ['api_key'], os.environ['api_secret_key'])
auth.set_access_token(os.environ['token_key'], os.environ['token_secret_key'])

api = tweepy.API(auth)

'''public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)'''

user = api.verify_credentials()
#print(user.name)
#print(user.followers_count)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.TweepyException:
        time.sleep(1000)


search_string = 'python'
numOfTweets = 2

for tweet in tweepy.Cursor(api.search_tweets, search_string).items(numOfTweets):
    try:
        tweet.retweet()
        print('Tweet rt')
    except tweepy.TweepyException as e:
        print(e.reason)
    except StopIteration:
        break

'''for follower in limit_handler(tweepy.Cursor(api.get_followers).items()):
    #print(follower.name)
    if follower.name == 'Jojo':
        follower.follow()'''