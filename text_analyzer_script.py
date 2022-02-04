'''# Import needed functionality
from text_analyzer import plot_counter, sum_counters
from collections import Counter


word_counts = Counter('ascwcsyswsscsfwwrrgrddewdqyc')

# Sum word_counts using "sum_counters" from "text_analyzer"
word_count_totals = sum_counters(word_counts)

# Plot word_count_totals using plot_counter from text_analyzer
plot_counter(word_counts)
'''

#----------------------------------------------------------------------------------------------------
# Because we used "from .document import Document, xx" in "__init__.py", no need pkg.module.class
from text_analyzer import SocialMedia, Tweets, Document
import json


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Lets find the most common words people are tweeting at this moment (say its a 10 mins tweet stream)
f_text = str()
with open('tweets3.txt', 'r') as file:
    for i in file:
        tweet = json.loads(i)
        text = tweet['text']
        f_text = f_text + ' ' + text

# create a new document instance from datacamp_tweets
datacamp_doc = Document(f_text)

# print the top 5 most used words in datacamp_doc
top_15_words = datacamp_doc.word_counts.most_common(15)
print(top_15_words)

#print(datacamp_doc.word_counts)  # Image what will happened




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Analysis full batch of tweet['text'], store in one str and plot the most-common hashtags & mentions
f_text = str()
with open('tweets3.txt', 'r') as file:
    for i in file:
        tweet = json.loads(i)
        text = tweet['text']
        f_text = f_text + ' ' + text


tweets = SocialMedia(text=f_text)

# Lets print top-5 hashtags & mentons on the screen
hashtags = tweets.hashtag_counts
print(hashtags.most_common(5))
mentions = tweets.mention_counts
print(mentions.most_common(5))

# Then lets plot most common 5 hashtags and mentions
SocialMedia.plot_counter(hashtags, 5)
SocialMedia.plot_counter(mentions, 5)




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Analysis full batch of tweet['text'], store in one str and plot the most-common hashtags & mentions
f_text = str()
with open('tweets3.txt', 'r') as file:
    for i in file:
        tweet = json.loads(i)
        text = tweet['text']
        f_text = f_text + ' ' + text


my_tweets = SocialMedia(f_text)

# Plot the most used hashtags in the retweets
hashtags = my_tweets.hashtag_counts
print(hashtags)

SocialMedia.plot_counter(hashtags, 6)





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# With a list to store each tweet['text'], analysis one by one; RTs,  hashtags, mentions, and plot them
words = list()
with open('tweets3.txt', 'r') as file:
    for i in file:
        tweet = json.loads(i)
        text = tweet['text']
        words.append(text)


i = 11

tweet = Tweets(words[i])
print(tweet.text)

rt = tweet.retweets
Tweets.plot_counter(rt.hashtag_counts, 3)
