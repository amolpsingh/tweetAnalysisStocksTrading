import tweepy
import re
from auth import *

#convert name of company to ticker to scrape information from yahoo finance
# def nameToTicker(name):

class processTweets:
   """clean tweets to run NLP sentiment analysis"""
   def processTweet(self, tweet):
      """
      Input is a tweet that it cleans by removing mentiones, hashtags, 
      links, punctuations and other nonalphanumeric characters.
      """
      #lowercase
      process = tweet.lower()
      #simplify contractions
      process = re.sub("'", "", process)
      #remove mentions
      process = re.sub("@[A-Za-z0-9_]+","", process)
      #remove hashtags
      process = re.sub("#[A-Za-z0-9_]+","", process)
      #remove links
      process = re.sub(r"http\S+", "", process)
      process = re.sub(r"www.\S+", "", process)
      #remve punctuations
      process = re.sub('[()!?]', ' ', process)
      process = re.sub('\[.*?\]',' ', process)
      #remove non alphanumeric characters
      process = re.sub("[^a-z0-9]"," ", process)
      return process

class twitterClient:
    """intialize twitter client to retrieve tweets"""
    def __init__(self):
       self.bearer_token = bearer_token
       self.client = tweepy.Client(self.bearer_token)
       self.tweet_cleaner = processTweets()


    def getTweetsForCompany(self, ticker):
      """
      Fetches the tweets from the twitter api and cleans the tweets and  
      """
      query = ticker
      file = "tweets.txt"
      tweets = []
      with open(file, 'a+') as fileHandler:
         for tweet in tweepy.Paginator(self.client.search_recent_tweets, query = query, tweet_fields=['context_annotations', 'created_at'], max_results=100).flatten(limit=10):
            proc = self.tweet_cleaner.processTweet(tweet.text)
            fileHandler.write('%s\n' % proc)
            tweets.append(proc)
      return tweets
