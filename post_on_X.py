import tweepy
from keys import *
import requests

Client = tweepy.Client( bearer_token=bearer_token, 
                        consumer_key=consumer_key, 
                        consumer_secret=consumer_secret, 
                        access_token=access_token, 
                        access_token_secret=access_token_secret, 
                        return_type = requests.Response,
                        wait_on_rate_limit=True)

#user = Client.get_user(username="ricardoparallax")
Client.create_tweet("Postagem feita via Pithon usando tweepy - Exemplo by @ricardoparallax")