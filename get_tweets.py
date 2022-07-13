from datetime import datetime
import os

import tweepy as tw

from UTILS.connect_twitter import orchestra_connect_twitter
from UTILS.twitter_objects import get_recently_tweets
from UTILS.view_results_query_twitter import view_result_query_twiter

# REALIZANDO A CONEXÃO COM O TWITTER
client = orchestra_connect_twitter()

# BUSCA SEM RETWEET
QUERY = "Bolsonaro OR Lula -is:retweet lang:pt"
LIMIT = 10
START_TIME = datetime(2022, 7, 11, 8, 0, 0)
END_TIME = datetime(2022, 7, 13, 0, 0, 0)

input = {
    "client": client,
    "query": QUERY,
    "limit": LIMIT,
    "start_time": START_TIME,
    "end_time": END_TIME
}

# OBTENDO OS RECENTES TWEETS USANDO A QUERY
validator, tweets, df_tweets = get_recently_tweets(**input)

if validator:

    # VISUALIZANDO O RESULTADO
    view_result_query_twiter(tweets)
