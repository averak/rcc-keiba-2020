import unittest
from post.text_builder import TextBuilder
from post.guide import Guide
from util.attr_util import AttrUtil
from util.model_util import ModelUtil


class TestPostTextBuilder(unittest.TestCase):
    def builder(self):
        return TextBuilder()

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
            ' 👑 %s\n 🔮 %s\n' % (horse, '★★★★☆'),
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

    @unittest.skip('投稿テキストのプレビュー')
    def test_make_text(self):
        race = ModelUtil.create_race(AttrUtil)
        horse = ModelUtil.create_horse(AttrUtil)
        guide = Guide()
        text = guide.construct(race, horse, 1.2)
        print()
        print(text)
