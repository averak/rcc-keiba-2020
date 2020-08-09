# -*- coding: utf-8 -*-
from . import attribute


class Name(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('名前がNoneです')
        if attr == '' or type(attr) is not str:
            raise Exception('名前は長さ1以上の文字列を指定してください')
