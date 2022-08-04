# Options Trading Bot based on Tweets

This python trading bot uses a custom dataset of >1 million as well as the kaggle dataset with >3 million tweets to train several models including varying architectures of LSTMs and transformers. Using the time series data from Yahoo Finance and public sentiment analyzed we are able to achieve a ~1% error on daily price prediction and using ablation experiments found in /experiments we see the there is predictive power in analyzing tweets.

This work was inspired by the growing dominace of social media and the famous market engineerng cases of $gme and $amc stock using reddit and twitter. This framework and trading bot was developed in python and utilizes twitter api2 and http requests to get the most recent tweets about specific companies in real time. Then, these tweets are analyzed with a transformer and with afinn model to determine a final sentiment score. This score is correlated with the previous closing prices using data from yfinance and then is used to train a LSTM model that acheives a high accuracy. The options are then bought using alpaca api. 

Data Sources: https://www.kaggle.com/datasets/omermetinn/tweets-about-the-top-companies-from-2015-to-2020
