import sys
import pandas as pd
import getAndProcessTweets
import sentimentModelHF

def main():
	"""
	"""
	try:
		args = sys.argv[1]
	except:
		raise Exception("Enter ticker symbol for stock")
	twitterClient = getAndProcessTweets.twitterClient()
	tweets = twitterClient.getTweetsForCompany(args)
	sentAnalModel = sentimentModelHF.sentAnalModel()
	tweets_analysis = []
	for tweet in tweets:
	    try:
	        sentiment_result = sentAnalModel.analysis(tweet)[0]
	        top_sentiment = max(sentiment_result, key=lambda x: x['score']) # Get the sentiment with the higher score
	        tweets_analysis.append({'tweet': tweet, 'sentiment': top_sentiment['label']})
	    except Exception as e:
	    	print(e)
	df = pd.DataFrame(tweets_analysis)
	sentiment_counts = df.groupby(['sentiment']).size()
	print(sentiment_counts)
	saved_model = tf.keras.models.load_model('saved_model/my_model')
	#should be afinn scores on df or try to transfer to hf model scores
	print(saved_model.predict(df))

if __name__ == '__main__':
	main()