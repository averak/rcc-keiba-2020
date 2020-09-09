from twitter import Twitter, OAuth
import json


class Poster:
    @classmethod
    def publish(cls, text):
        token = cls.token()
        twitter = Twitter(auth=OAuth(*token))

        return twitter.statuses.update(status=text)

    @classmethod
    def token(cls):
        with open('config/twitter_token.json', 'r') as f:
            token = json.load(f)

        return token.values()
