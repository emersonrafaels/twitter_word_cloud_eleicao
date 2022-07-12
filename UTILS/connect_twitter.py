from inspect import stack

from dynaconf import settings
import tweepy
import requests


def orchestra_connect_twitter():

    # INICIANDO O CLIENT
    client = None

    try:
        # AUTENTICANDO
        client = tweepy.Client(bearer_token=settings.SEARCHTWEETS_BEARER_TOKEN,
                               consumer_key=settings.SEARCHTWEETS_CONSUMER_KEY,
                               consumer_secret=settings.SEARCHTWEETS_CONSUMER_SECRET,
                               access_token=settings.SEARCHTWEETS_ACCESS_TOKEN,
                               access_token_secret=settings.SEARCHTWEETS_ACCESS_TOKEN_SECRET,
                               return_type=requests.Response,
                               wait_on_rate_limit=True)

    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return client