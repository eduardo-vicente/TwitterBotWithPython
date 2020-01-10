import tweepy
from requests_oauthlib import OAuth2Session, OAuth1Session

print('this is my twitter bot')

CONSUMER_KEY = 'XCe5mrMSpDt16HAV62WY3pRiq'
CONSUMER_SECRET = 'hjod9uD1cmXvGt4vBaUIDUVdUTiXXh5J0XHRQOqk2p7WF6jx3G'
ACCESS_KEY = '1215408809201545216-4EN2ztfWpidgaOLxbqj6wT2eRf1NWm'
ACCESS_SECRET = 'PSvZgRE7OAWDZBvCLsMNE9a3AF8FymalwY1ue1JxWom1s'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



