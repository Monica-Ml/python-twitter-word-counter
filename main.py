import tweepy
import collections
import re
from rich import print
import matplotlib.pyplot as plt

bearer_token = "" # Your Bearer Token here

def get_user_tweets(bearer_token,user_id):
    client = tweepy.Client(bearer_token)
    response = client.get_users_tweets(user_id, max_results=100)
    big_data=''
    for tweet in response.data:
        big_data=big_data+' '+str(tweet.text.encode("utf-8").decode("utf-8"))
    return big_data

def normalize_data(input_str):
    data_str = input_str.lower()
    data_str = data_str.strip()
    data_str=re.sub('[^A-Za-z0-9 ]+', '', data_str)
    data_array=data_str.split(' ')
    #print(data_array)
    print('================================================================================================================================================')
    print('Total words: '+str(len(data_array)))
    print('================================================================================================================================================')
    return data_array

def detect_word_count(data_array):
    word_counts = collections.Counter(data_array)
    chart_words_array = []
    chart_words_count_array = []
    for word, count in sorted(word_counts.items()):
        print('"%s" (%d)%s' % (word, count, " [red]********[/]" if count > 3 else ""))
        print('____________________________________________________________')
        chart_words_array.append(word)
        chart_words_count_array.append(count)
    print('Finish')

    colors = ['r', 'y', 'g', 'b']
    plt.pie(chart_words_count_array, labels = chart_words_array, colors=colors, startangle=90, radius = 1.2, autopct = '%1.1f%%')
    plt.legend()
    plt.show()

print('Start script...')
user_id = # Your target user_id (Integer), example: 1480426819430006751
big_data=get_user_tweets(bearer_token,user_id)
data_array=normalize_data(big_data)
detect_word_count(data_array)
