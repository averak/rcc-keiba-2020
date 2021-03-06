class TextBuilder:
    def __init__(self):
        self.__buffer = ''

    def make_title(self, title):
        self.__buffer += '【%s】' % title
        self.new_line()

    def make_string(self, string):
        self.__buffer += str(string)
        self.new_line()

    def make_forecast(self, horse, score):
        self.__buffer += ' 🔮 一位予想馬'
        self.new_line()
        self.__buffer += ' 👑 %s' % horse
        self.new_line()

    def make_horses(self, horses):
        self.__buffer += '▼ 出場馬'
        self.new_line()
        for horse in horses:
            self.__buffer += '🐎 %s' % horse
            self.new_line()

    def make_hashtag(self, *tag):
        self.__buffer += '#%s' % ' #'.join(tag)

    def new_line(self):
        self.__buffer += '\n'

    def get_result(self):
        return self.__buffer

    def clear(self):
        self.__buffer = ''

    def __make_star(self, score):
        result = '★' * round(float(score))
        result = result.ljust(5, '☆')
        return result
