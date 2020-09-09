from .text_builder import TextBuilder


class Guide:
    def __init__(self, builder=TextBuilder()):
        self.__builder = builder

    def construct(self, **args):
        # タイトル
        self.__builder.make_title('本日の競馬予想')
        self.__builder.new_line()

        # レース情報
        self.__builder.make_string(args['race_data'])
        self.__builder.new_line()

        # 予想結果
        self.__builder.make_string('━━━━━━━━━━━━━━━')
        self.__builder.make_forecast(args['winner'].name, args['winner_score'])
        self.__builder.make_string('━━━━━━━━━━━━━━━')
        self.__builder.new_line()

        # 出場馬一覧
        horses = [horse.name for horse in args['horses']][:3]
        horses.append('...')
        self.__builder.make_horses(horses)
        self.__builder.new_line()

        # 詳細URL
        self.__builder.make_string(args['race_url'])

        return self.__builder.get_result()
