import json
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

API_Key = 'sOJIMCij96R6fz39KVOt29q3O'
API_Secret_Key = 'mJdBivvK4Z5iRoai1RvIiXy1gIjTdqq2Hg3Gn2CUJdU5eJmmJe'
Bearer_Token = 'AAAAAAAAAAAAAAAAAAAAAK%2B%2FJwEAAAAAgynG73KjbqUA1GD0yoVuDw4%2Bw%2Bs%3DFmTWjqhQAcr9PSz7XMDhUX0MGMf5opVYi36NTF9v5jpkWKqran'
Access_Token = '582946827-ppR1YRNNbl9KbtFnpOt301IUCHMz1GhANodt4Jc1'

Access_Token_Secret = 'WiyEy4vMOjsS1iWKDYl9QKg8ue0TbxpR8XqEbqMIPnBNE'

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
