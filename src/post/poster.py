import os
from twitter import Twitter, OAuth


class Poster:
    @classmethod
    def publish(cls, text):
        token = cls.token()
        twitter = Twitter(auth=OAuth(*token))

        return twitter.statuses.update(status=text)

    @classmethod
    def token(cls):
        result = []
        result.append(os.environ['TWITTER_ACCESS_TOKEN'])
        result.append(os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
        result.append(os.environ['TWITTER_API_KEY'])
        result.append(os.environ['TWITTER_API_KEY_SECRET'])

        return result
