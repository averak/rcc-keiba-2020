import unittest
from post import Guide, Poster, TextBuilder
from util.attr_util import AttrUtil
from util.model_util import ModelUtil


class TestPostTextBuilder(unittest.TestCase):
    def builder(self):
        return TextBuilder()

    def make_text(self):
        race = ModelUtil.create_race(AttrUtil)
        horse = ModelUtil.create_horse(AttrUtil)
        guide = Guide()
        return guide.construct(race, horse, 1.2)

    def test_make_title(self):
        title = 'テストタイトル'
        builder = self.builder()
        builder.make_title(title)

        self.assertEqual(
            '【%s】\n' % title,
            builder.get_result()
        )

    def test_make_string(self):
        string = 'テスト文字列'
        builder = self.builder()
        builder.make_string(string)

        self.assertEqual(
            '%s\n' % string,
            builder.get_result()
        )

    def test_make_forecast(self):
        horse = '優勝馬名'
        score = 3.8
        builder = self.builder()
        builder.make_forecast(horse, score)

        self.assertEqual(
            ' 🔮 一位予想馬\n 👑 %s\n' % horse,
            builder.get_result()
        )

    def test_make_horse(self):
        horses = ['馬1', '馬2', '馬3']
        builder = self.builder()
        builder.make_horses(horses)

        self.assertEqual(
            '▼ 出場馬\n🐎 %s\n🐎 %s\n🐎 %s\n' % (
                horses[0], horses[1], horses[2]),
            builder.get_result()
        )

    def test_make_hashtag(self):
        builder = self.builder()
        builder.make_hashtag('タグA', 'タグB')

        self.assertEqual('#タグA #タグB', builder.get_result())

    def test_make_text(self):
        self.make_text()

    @unittest.skip('トークン非公開のため')
    def test_twitter_token(self):
        token = Poster.token()
        self.assertEqual(4, len(token))

    @unittest.skip('投稿されるため')
    def test_post(self):
        Poster.publish(self.make_text())
