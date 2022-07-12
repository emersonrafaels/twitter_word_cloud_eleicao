from datetime import datetime
from inspect import stack

import tweepy as tw
import pandas as pd


def get_recently_tweets(client, query, limit, kwargs):

    # INICIANDO AS VARIÁVEIS DE RESULTADOS
    validator = False
    tweets = tweets_data = df = []

    try:
        # REALIZANDO A OBTENÇÃO DOS TWEETS
        tweets = client.search_recent_tweets(query=query,
                                             max_results=limit)

        # SALVANDO OS RESULTADOS COMO JSON
        tweets_dict = tweets.json()

        # OBTENDO OS DADOS
        tweets_data = tweets_dict['data']

        # OBTENDO UM DATAFRAME
        df = pd.json_normalize(tweets_data)

        validator = True

    except Exception as ex:
        print("ERRO NA FUNÇÃO {} - {}".format(stack()[0][3], ex))

    return validator, tweets_data, df