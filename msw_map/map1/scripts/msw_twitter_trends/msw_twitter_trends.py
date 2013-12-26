import twitter
import json
import time
from twitter import *

api = twitter.Api()

api = twitter.Api(consumer_key='E7RaWBHZiNjFm1OijP3pg',
	consumer_secret='5ikpryQmuWFf51YSncdbtZoQKb2DoZOCX6fYud0o',
	access_token_key='267395308-Xf2PZEjccqRBbBwYPkHtysT365W3CWtN6hYVRjlw',
	access_token_secret='17KrqiIqKyJhnMKspVJvMA3qUp4VazqeppWgMpawE6nIP')
'''
#print api.VerifyCredentials()
statuses = api.GetUserTimeline('JGWitkowski')

for s in statuses:
	print s.text + "\n"
'''
#Create a class for top 10 trends in a location
#store the trends, current tweets about those trends

class MyTrends:
	def __init__(self):
		self.trends = []
		self.locationId = 23424977
		self.trend_tweets = {}
		self.api = twitter.Api()
		#authenticate Twitter API, eventually pass in your own OAuth settings
	def authApi(self):
		self.api = twitter.Api(consumer_key='E7RaWBHZiNjFm1OijP3pg',
			consumer_secret='5ikpryQmuWFf51YSncdbtZoQKb2DoZOCX6fYud0o',
			access_token_key='267395308-Xf2PZEjccqRBbBwYPkHtysT365W3CWtN6hYVRjlw',
			access_token_secret='17KrqiIqKyJhnMKspVJvMA3qUp4VazqeppWgMpawE6nIP')

	def setTrends(self):
		raw_trends = api.GetTrendsWoeid(self.locationId)
		for raw in raw_trends:
			self.trends.append(raw.name)
	def getTrends(self):
		return self.trends
	def printTrends(self):
		for t in self.trends:
			print t
	def setTweets(self):
		for t in self.trends:
			raw_tweets = self.api.GetSearch(t, count=100)
			print("T")
			time.sleep(0.5)
			self.trend_tweets[t] = []
			for r in raw_tweets:
				self.trend_tweets[t].append(r.text) 
	def getWords(self, trend):
		words = []
		for t in self.trend_tweets:
			words += [ w for w in t.split()]
		return words
	def lexicalDiversity(self, trend):
		words = self.getWords(trend)
		lexd = 1.0 * len(set(words))/len(words)
		return lexd
	def wordsPerTweet(self, trend):
		words = self.getWords(trend)
		wpt = 1.0* sum([ len(w.split()) for w in words])/len(words)
		return wpt

#Testing
print("Twitter Trends Started")
mt = MyTrends()
print ("Authenticating...")
mt.authApi()
print("Retrieving Current Trends...")
mt.setTrends()
print("Current Trends:")
mt.printTrends()
print("Getting Tweets From Those Trends...")
mt.setTweets()
print mt.lexicalDiversity(mt.getTrends()[0])
print mt.wordsPerTweet(mt.getTrends()[0])
'''
#lexcial diversity
lexd = 1.0*len(set(words))/len(words)
print "Lexical Diversity: " + str(lexd)

#avg words per tweet
wpt = 1.0*sum([ len(t.split()) for t in trends])/len(trends)
print "Words Per Tweet: " + str(wpt) 
'''
