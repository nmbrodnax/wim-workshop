import csv
import sys
from requests_oauthlib import OAuth1Session


# get authentication parameters from local file
local_file = '/Users/nbrodnax/Indiana/CEWIT/twitter_auth.txt'
with open(local_file) as txtfile:
    contents = txtfile.readline()
    credentials = eval(contents.strip('\n'))

# api OAuth 1.0 authentication
twitter = OAuth1Session(
    credentials.get('consumer_key'),
    client_secret=credentials.get('consumer_secret'),
    resource_owner_key=credentials.get('access_token'),
    resource_owner_secret=credentials.get('access_secret')
)

# host location of api
host = 'https://api.twitter.com'

# api GET request for user ids of followers
get_path = '/1.1/search/tweets.json?q=%40IUBloomington'
url = host + get_path
response = twitter.get(url)

# check the HTTP response code
print(response)

# parse the JSON data into a python object
tweets = response.json()

# check the structure of the data
print(len(tweets))
print(type(tweets))
print(tweets.keys())
print(len(tweets['statuses']))

# encode uncommon characters
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

print(str(tweets['statuses']).translate(non_bmp_map))
