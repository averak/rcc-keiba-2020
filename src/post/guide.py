from .text_builder import TextBuilder


class Guide:
    def __init__(self, builder=TextBuilder()):
        self.__builder = builder

    def construct(self, race, winner, score):
        # タイトル
        self.__builder.make_title('本日の競馬予想')
        self.__builder.new_line()

        # レース情報
        self.__builder.make_string(race.name)
        self.__builder.make_string(
            '%sm（%s|%s周り）' % (race.distance, race.field, race.turn))
        self.__builder.make_string('賞金：%s' % race.prize)
        self.__builder.new_line()

        # 予想結果
        self.__builder.make_string('━━━━━━━━━━━━━━━')
        self.__builder.make_forecast(winner.name, score)
        self.__builder.make_string('━━━━━━━━━━━━━━━')
        self.__builder.new_line()

        # 出場馬一覧
        horses = [race_horse.name for race_horse in race.horses][:2]
        horses.append('...')
        self.__builder.make_horses(horses)
        self.__builder.new_line()

        # 詳細URL
        self.__builder.make_string(race.url)

        result = self.__builder.get_result()
        self.__builder.clear()

        return result
