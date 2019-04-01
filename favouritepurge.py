import tweepy
import time

consumer_key = "[key goes here]"
consumer_secret = "[secret key goes here]"
access_token = '[access token goes here]'
access_token_secret = '[secret access token goes here]'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for i in range(0,1000):
   lib = api.favorites()

   try:
      for tweet in lib: 
       api.destroy_favorite(tweet.id)
       print('Purged!')
   except:
       print('All done!')
       break
