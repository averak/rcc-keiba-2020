from .text_builder import TextBuilder


class Guide:
    def __init__(self, builder=TextBuilder()):
        self.__builder = builder

    def construct(self, race, winner, score):
        # タイトル
        self.__builder.make_title('本日の競馬予想')
        self.__builder.new_line()

        # レース情報
        self.__builder.make_string(
            '%sm（%s|%s周り）' % (race.distance, race.field, race.turn))
        self.__builder.new_line()

        # 予想結果
        self.__builder.make_string('━━━━━━━━━━━━━━━')
        self.__builder.make_forecast(winner.name, score)
        self.__builder.make_string('━━━━━━━━━━━━━━━')
        self.__builder.new_line()

        # 出場馬一覧
        horses = [horse.name for horse in race.horses][:3]
        horses.append('...')
        self.__builder.make_horses(horses)
        self.__builder.new_line()

        # 詳細URL
        self.__builder.make_string(race.url)

        return self.__builder.get_result()
