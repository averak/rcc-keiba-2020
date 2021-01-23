import unittest
import tweet
from tweet import Tweet, Guide, TextBuilder
from util.attr_util import AttrUtil
from util.model_util import ModelUtil


class TestTweet(unittest.TestCase):
    def setUp(self):
        self.guide = Guide()
        self.text_builder = TextBuilder()

    def make_text(self):
        race = ModelUtil.create_race(AttrUtil)
        horse = ModelUtil.create_horse(AttrUtil)
        return self.guide.construct(race, horse, 1.2)

    def test_make_title(self):
        title = 'テストタイトル'
        self.text_builder.clear()
        self.text_builder.make_title(title)

        self.assertEqual(
            '【%s】\n' % title,
            self.text_builder.get_result()
        )

    def test_make_string(self):
        string = 'テスト文字列'
        self.text_builder.clear()
        self.text_builder.make_string(string)

        self.assertEqual(
            '%s\n' % string,
            self.text_builder.get_result()
        )

    def test_make_forecast(self):
        horse = '優勝馬名'
        score = 3.8
        self.text_builder.clear()
        self.text_builder.make_forecast(horse, score)

        self.assertEqual(
            ' 🔮 一位予想馬\n 👑 %s\n' % horse,
            self.text_builder.get_result()
        )

    def test_make_horse(self):
        horses = ['馬1', '馬2', '馬3']
        self.text_builder.clear()
        self.text_builder.make_horses(horses)

        self.assertEqual(
            '▼ 出場馬\n🐎 %s\n🐎 %s\n🐎 %s\n' % (
                horses[0], horses[1], horses[2]),
            self.text_builder.get_result()
        )

    def test_make_hashtag(self):
        self.text_builder.clear()
        self.text_builder.make_hashtag('タグA', 'タグB')

        self.assertEqual('#タグA #タグB', self.text_builder.get_result())

    def test_make_text(self):
        self.make_text()

    def test_twitter_token(self):
        token = Tweet.token()
        self.assertEqual(4, len(token))

    @unittest.skip('TESTSKIP')
    def test_post(self):
        tweet.tweet.publish(self.make_text())
