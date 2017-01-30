# coding: utf-8
from streaming_api import filter

# Replace keys with your own keys
APIKEYS = dict(
    CONSUMER='consumer key',
    CONSUMER_SECRET='consumer secret key',
    ACCESS_TOKEN='access token key',
    ACCESS_TOKEN_SECRET='access token secret key')

# Geometory of Japan
params = {"locations": "122.56, 20.25, 153.60, 45.34"}

# NOTICE: this script may shows delimited output in your terminal
res = filter(APIKEYS, params)
for tweet_json_str in res:
    print tweet_json_str
