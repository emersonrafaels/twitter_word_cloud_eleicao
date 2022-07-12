from datetime import datetime
import os

import tweepy as tw
from tabulate import tabulate

from UTILS.connect_twitter import orchestra_connect_twitter
from UTILS.twitter_objects import get_recently_tweets

# REALIZANDO A CONEXÃO COM O TWITTER
client = orchestra_connect_twitter()

# BUSCA SEM RETWEET
QUERY = "Bolsonaro OR Lula -is:retweet lang:pt"
LIMIT = 10
START_TIME = datetime(2022, 7, 5, 10, 10, 10)
END_TIME = datetime(2022, 7, 12)


TWETTS_ADITIONAL_ARGS = {"START_TIME": START_TIME,
                         "END_TIME": END_TIME}

# OBTENDO OS RECENTES TWEETS USANDO A QUERY
validator, tweets, df_tweets = get_recently_tweets(client=client,
                                                   query=QUERY,
                                                   limit=LIMIT,
                                                   kwargs=TWETTS_ADITIONAL_ARGS)


if validator:

    # VISUALIZANDO OS DADOS UTILIZANDO TABULATE
    print(tabulate(tweets, headers="keys"))

    # PERCORRENDO CADA UM DOS DADOS OBTIDOS
    for tweet in tweets:
        print(tweet["id"])
        print(tweet["text"])
        print("-"*50)
