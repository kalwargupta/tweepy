#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 12:17:51 2019

@author: jeetu
"""
#importing the liabraries
from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

# method to calculate the percentage
def percentage(part, whole):
    return 100 * float(part)/float(whole)

#putting the authentication keys
consumer_key = "HJwMt2iAP7gIGifvC5eGh6LT0"
consumer_secret = "LNThhAQIzx2s4x7lwW7RKNK65oK9Fn4LXv6fVHj6ROXxGOSQsh"
access_key = "4653388886-dWUexCGAaUEEoytj4HqavtuTpFkvap2q93DOnKw"
access_secret = "QB6IQHLCES2m1KoOiASQ3GieItewZ8AEvekqUd01qZops"


# authentication
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api=tweepy.API(auth)

# getting inputs from the user
searchTerm=input("Enter the topic to be searched:- ")
noOfSearch=int (input("enter the number of tweets :- "))

tweets= tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearch)


positive =0
negative=0
neutral=0
polarity=0

#extracting the tweets and Analyzing it
for tweet in tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    polarity +=analysis.sentiment.polarity
    
    if (analysis.sentiment.polarity==0):
        neutral+=1
    elif (analysis.sentiment.polarity>0.00):
        positive+=1
    elif (analysis.sentiment.polarity<0.00):
        negative+=1
        
        
# calculating percentage
positive=percentage(positive,noOfSearch)
negative=percentage(negative,noOfSearch)
neutral=percentage(neutral,noOfSearch)
polarity=percentage(polarity,noOfSearch)

#Decimal format
positive=format(positive,".2f")
negative=format(negative,".2f")
neutral =format(neutral,".2f")


#output
print("How people are reacting on " + searchTerm + "by analyzing "+ str(noOfSearch)+"Tweets")

if (polarity==0):
    print("Neutral")
if (polarity>0.00):
    print("Positive")
if (polarity<0.00):
    print("Negative")
    
labels=['Positive['+str(positive)+'%]','Negative['+str(negative)+'%]','Neutral['+str(neutral)+'%]']
sizes=[positive, negative, neutral]
colors=['yellowgreen','red','gold']
patches,texts=plt.pie(sizes,colors=colors, startangle=90)
plt.legend(patches,labels,loc="best")
plt.title( "How people are reacting on " + searchTerm + "by analyzing "+ str(noOfSearch)+"Tweets")
plt.axis('equal')
plt.tight_layout()
plt.show()
        
        
        
        
        
        
        