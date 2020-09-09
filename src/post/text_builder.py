class TextBuilder:
    def __init__(self):
        self.__buffer = ''

    def make_title(self, title):
        self.__buffer += '【%s】' % title
        self.new_line()

    def make_string(self, string):
        self.__buffer += string
        self.new_line()

    def make_forecast(self, horse, score):
        self.__buffer += ' 👑 ' + horse
        self.new_line()
        self.__buffer += ' 🔮 ' + self.__make_star(score)
        self.new_line()

    def make_horses(self, horses):
        self.__buffer += '▼ 出場馬'
        self.new_line()
        for horse in horses:
            self.__buffer += '🐎 ' + horse
            self.new_line()

    def new_line(self):
        self.__buffer += '\n'

    def get_result(self):
        return self.__buffer

    def __make_star(self, score):
        result = '★' * round(score)
        result = result.ljust(5, '☆')
        return result
