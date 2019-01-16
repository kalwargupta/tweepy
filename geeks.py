#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 18:11:06 2019

@author: jeetu
"""

import tweepy 

# Fill the X's with the credentials obtained by 
# following the above mentioned procedure. 
consumer_key = "aKTdf2AhAgCK6nYfYcOtwAAci"
consumer_secret = "tpsAauHk0fW59oF8aSX9jpD7uV25CPNwAWlCrrtYZcQNknK7xR"
access_key = "4653388886-LPgvWLxNaMNdfhBrgqM6T73ZrH0gMeQyioeH0fx"
access_secret = "Kj4gIXx3dALycQnIzl0ARLyTKG2EQAy5v26SQCKs4vZuz"

# Function to extract tweets 
def get_tweets(username): 
		
		# Authorization to consumer key and consumer secret 
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

		# Access to user's access key and access secret 
		auth.set_access_token(access_key, access_secret) 

		# Calling api 
		api = tweepy.API(auth) 

		# 200 tweets to be extracted 
		number_of_tweets=20
		tweets = api.user_timeline(screen_name=username) 

		# Empty Array 
		tmp=[] 

		# create array of tweet information: username, 
		# tweet id, date/time, text 
		tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
		for j in tweets_for_csv: 

			# Appending tweets to the empty array tmp 
			tmp.append(j) 

		# Printing the tweets 
		print(tmp) 


# Driver code 
if __name__ == '__main__': 

	# Here goes the twitter handle for the user 
	# whose tweets are to be extracted. 
	get_tweets("jeetu ") 
