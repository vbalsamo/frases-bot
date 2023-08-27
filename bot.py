import random
import os
import tweepy
from frases import frases

client = tweepy.Client(
    consumer_key=os.environ['API_KEY'],
    consumer_secret=os.environ['API_KEY_SECRET'],
    access_token=os.environ['ACCESS_TOKEN'],
    access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
)

client.create_tweet(text=random.choice(frases))
