# coding: utf-8
import urllib2
import oauth2


def filter(APIKEYS, params):
    consumer = oauth2.Consumer(
        key=APIKEYS['CONSUMER'], secret=APIKEYS['CONSUMER_SECRET'])
    token = oauth2.Token(
        key=APIKEYS['ACCESS_TOKEN'], secret=APIKEYS['ACCESS_TOKEN_SECRET'])

    url = 'https://stream.twitter.com/1.1/statuses/filter.json'

    request = oauth2.Request.from_consumer_and_token(
        consumer, token, http_url=url, parameters=params)
    request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    res = urllib2.urlopen(request.to_url())
    return res


def sample(APIKEYS):
    consumer = oauth2.Consumer(
        key=APIKEYS['CONSUMER'], secret=APIKEYS['CONSUMER_SECRET'])
    token = oauth2.Token(
        key=APIKEYS['ACCESS_TOKEN'], secret=APIKEYS['ACCESS_TOKEN_SECRET'])

    url = 'https://stream.twitter.com/1.1/statuses/sample.json'

    request = oauth2.Request.from_consumer_and_token(
        consumer, token, http_url=url)
    request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    res = urllib2.urlopen(request.to_url())
    return res
