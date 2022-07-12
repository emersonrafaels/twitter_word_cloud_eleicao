import pandas as pd


def execute_filter_candidatos(tweets, list_candidatos):

    # INICIANDO A VARIÁVEL QUE ARMAZENARÁ A LISTA DE PALAVRAS
    list_words = []

    # PERCORRENDO CADA TWEET
    for value in tweets:

        # ARMAZENANDO O RESULTADO DO SPLIT NA LISTA DE PALAVRAS
        for word in value.split(" "):

            for filter_candidato in list_candidatos:

                if word.upper().find(filter_candidato) != -1:
                    list_words.append([word.upper(), filter_candidato])

    return list_words

# REALIZANDO A ABERTURA DO ARQUIVO DE RESULTADO DOS TWEETS
with open("RESULTADO_TWEETS.txt", mode="r") as tweet_result:

    tweets = tweet_result.readlines()
    tweet_result.close()

# FILTRANDO TWEETS COM LULA OU BOLSONARO
filter_candidatos = ["LULA", "BOLSONARO"]


list_words = execute_filter_candidatos(tweets=tweets,
                                       list_candidatos=filter_candidatos)

df = pd.DataFrame(list_words, columns=["WORDS", "CANDIDATO"])

df_groupby_candidato = df.groupby("CANDIDATO").count().reset_index()

df_groupby_candidato["PERCENT"] = round(100*(df_groupby_candidato["WORDS"] / df_groupby_candidato["WORDS"].sum()), 2)

print(df_groupby_candidato)


