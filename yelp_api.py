from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from os import environ

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())



def get_businesses(term, location):	
    params = {
        'term': term,
        'lang': 'en',
        'limit': 3,
        'sort': 2
    }

    auth = Oauth1Authenticator(
    consumer_key=environ['CONSUMER_KEY'],
    consumer_secret=environ['CONSUMER_SECRET'],
    token=environ['TOKEN'],
    token_secret=environ['TOKEN_SECRET']
    )

    client = Client(auth)

    response = client.search(location, **params)

    return response.businesses

