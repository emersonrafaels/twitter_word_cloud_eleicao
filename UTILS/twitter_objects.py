from datetime import datetime
from inspect import stack

import tweepy as tw
import pandas as pd
from pydantic import validate_arguments, ValidationError
from typing import Optional, Union


@validate_arguments(config=dict(arbitrary_types_allowed=True))
def get_recently_tweets(client: tw.client.Client,
                        query: str,
                        limit: int = 10,
                        start_time: Optional[Union[str, datetime]] = None,
                        end_time: Optional[Union[str, datetime]] = None):

    # INICIANDO AS VARIÁVEIS DE RESULTADOS
    validator = False
    tweets = tweets_data = df = []

    try:
        # REALIZANDO A OBTENÇÃO DOS TWEETS
        tweets = client.search_recent_tweets(query=query,
                                             max_results=limit,
                                             start_time=start_time,
                                             end_time=end_time,
                                             tweet_fields=['author_id',
                                                           'created_at',
                                                           'text',
                                                           'source',
                                                           'lang',
                                                           'geo'],
                                             user_fields=['name',
                                                          'username',
                                                          'location',
                                                          'verified'],
                                             expansions=['geo.place_id',
                                                         'author_id'],
                                             place_fields=['country',
                                                           'country_code'])

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