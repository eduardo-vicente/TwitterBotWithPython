from requests_oauthlib import OAuth1Session

creds = open('credentials.txt').readlines()

session = OAuth1Session(creds[0].strip(), creds[1].strip(), creds[2].strip(), creds[3].strip())

params = {'status': 'hello world'}

url = 'https://api.twitter.com/1.1/statuses/update.json'

session.post(url,params=params)
