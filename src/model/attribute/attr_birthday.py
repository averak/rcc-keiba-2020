# -*- coding: utf-8 -*-
import re
from . import attribute


class Birthday(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('誕生日がNoneです')
        if type(attr) is not str:
            raise Exception('誕生日は"YYYY年MM月DD日"のフォーマットで指定してください')
        if re.fullmatch(r'\d{4}年\d{1,2}月\d{1,2}日', attr) is None:
            raise Exception('誕生日は"YYYY年MM月DD日"のフォーマットで指定してください')
