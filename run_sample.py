# coding: utf-8
from streaming_api import sample

# Replace keys with your own keys
APIKEYS = dict(
    CONSUMER='consumer key',
    CONSUMER_SECRET='consumer secret key',
    ACCESS_TOKEN='access token key',
    ACCESS_TOKEN_SECRET='access token secret key')

# NOTICE: this script shows delimited output in your terminal
res = sample(APIKEYS)
for tweet_json_str in res:
    print tweet_json_str
