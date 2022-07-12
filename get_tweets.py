import os

from dynaconf import settings
import tweepy

# OBTENDO AS CONFIGURAÇÕES DE AUTENTICAÇÃO
auth = tweepy.OAuth1UserHandler(
    settings.SEARCHTWEETS_CONSUMER_KEY,
    settings.SEARCHTWEETS_CONSUMER_SECRET,
    settings.SEARCHTWEETS_ACCESS_TOKEN,
    settings.SEARCHTWEETS_ACCESS_TOKEN_SECRET
)

# AUTENTICANDO
client = tweepy.Client(settings.SEARCHTWEETS_BEARER_TOKEN)

# BUSCA
QUERY = "Bolsonaro OR Lula lang:pt"
LIMIT = 60

# REALIZANDO A OBTENÇÃO DOS TWEETS
tweets = client.search_recent_tweets(QUERY,
                                     max_results=LIMIT).data

# INICIANDO UMA LISTA PARA ARMAZENAR AS INFORMAÇÕES
list_result = []

for tweet in tweets:
    print(tweet.id)
    print(tweet.text)
    print("-"*50)
    list_result.append([str(tweet.id), str(tweet.text)])

with open("RESULTADO_TWEETS.txt", mode="a") as list_result_tweets:

    for line in list_result:

        try:
            list_result_tweets.write("ID: {0} - TEXTO: {1}\n".format(line[0],
                                                                     line[1]))
        except Exception as ex:
            print(ex)
