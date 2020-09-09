import re
from . import attribute


class Birthday(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('誕生日は"YYYY年MM月DD日"のフォーマットで指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) is not str:
            return False
        if re.fullmatch(r'\d{4}年\d{1,2}月\d{1,2}日', attr) is None:
            return False

        return True
