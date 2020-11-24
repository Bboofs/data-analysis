import json
import config as cf
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

API_Key = cf.consumer_key
API_Secret_Key = cf.consumer_secret
Access_Token = cf.access_token
Access_Token_Secret = cf.access_token_secret

auth = OAuthHandler(API_Key, API_Secret_Key)
auth.set_access_token(Access_Token, Access_Token_Secret)


class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':  # remove retweets
            print(status.text)
            print(status.author.screen_name, status.created_at, status.source, '\n')

    def on_error(self, status_code):
        print('Error code: {}'.format(status_code))
        return True  # Keep stream alive

    def on_timeout(self):
        print('Listener timed out')
        return True  # Keep stream alive


def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)


def pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))


if __name__ == '__main__':
    # print_to_terminal()
    pull_down_tweets(auth.username)
