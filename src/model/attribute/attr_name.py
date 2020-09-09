from . import attribute


class Name(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('名前は1文字以上の文字列を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) is not str:
            return False
        if attr == '':
            return False

        return True
