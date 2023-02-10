import random
import os
import tweepy

consumerKey = os.environ['API_KEY']
consumerSecret = os.environ['API_KEY_SECRET']
accessKey = os.environ['ACCESS_TOKEN']
accessSecret = os.environ['ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessKey, accessSecret)
api = tweepy.API(auth)

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
        if random.randrange(num):
            continue
        line = aline
    return line

api.update_status(status = random_line(open('frases_convertido.txt')))