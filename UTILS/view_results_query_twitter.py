from tabulate import tabulate


def view_result_query_twiter(tweets={}):

    # VISUALIZANDO OS DADOS UTILIZANDO TABULATE
    print(tabulate(tweets, headers="keys"))

    # PERCORRENDO CADA UM DOS DADOS OBTIDOS
    for tweet in tweets:
        for key in tweet.keys():
            print("{} - {}".format(key, tweet[key]))
        print("-"*50)