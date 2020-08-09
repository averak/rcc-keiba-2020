# -*- coding: utf-8 -*-


class Attribute:
    def __init__(self, attr):
        self._restrict(attr)
        self.__attr = attr

    def _restrict(self, attr):
        raise Exception('サブクラスの責務')

    def get_attr(self):
        return self.__attr
