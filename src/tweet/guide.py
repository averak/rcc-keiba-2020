from .text_builder import TextBuilder


class Guide:
    def __init__(self, builder=TextBuilder()):
        self.__builder = builder

    def construct(self, race, winner, score):
        # タイトル
        self.builder.make_title('本日の競馬予想')
        self.builder.new_line()

        # レース情報
        self.builder.make_string(race.name)
        self.builder.make_string(
            '%sm（%s|%s周り）' % (race.distance, race.field, race.turn))
        self.builder.make_string('賞金：%s' % race.prize)
        self.builder.new_line()

        # 予想結果
        self.builder.make_string('━━━━━━━━━━━━━━━')
        self.builder.make_forecast(winner.name, score)
        self.builder.make_string('━━━━━━━━━━━━━━━')
        self.builder.new_line()

        # 出場馬一覧
        horses = [race_horse.name for race_horse in race.horses][:2]
        horses.append('...')
        self.builder.make_horses(horses)
        self.builder.new_line()

        # ハッシュタグ
        self.builder.make_hashtag('競馬予想', '立命の母')
        self.builder.new_line()
        self.builder.new_line()

        # 詳細URL
        self.builder.make_string(race.url)

        result = self.builder.get_result()
        self.builder.clear()

        return result

    @property
    def builder(self):
        return self.__builder
