import os
from twitter import Twitter, OAuth


class Tweet:
    tokens = [
        'TWITTER_ACCESS_TOKEN',
        'TWITTER_ACCESS_TOKEN_SECRET',
        'TWITTER_API_KEY',
        'TWITTER_API_KEY_SECRET'
    ]

    @classmethod
    def publish(cls, text):
        if not cls.is_valid():
            return

        token = cls.token()
        twitter = Twitter(auth=OAuth(*token))

        return twitter.statuses.update(status=text)

    @classmethod
    def token(cls):
        if cls.is_valid():
            return [os.environ[env] for env in cls.tokens]
        else:
            return ['' for env in cls.tokens]

    @classmethod
    def is_valid(cls):
        for env in cls.tokens:
            if env not in os.environ:
                return False
        return True
