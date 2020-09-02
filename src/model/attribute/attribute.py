# -*- coding: utf-8 -*-


class Attribute:
    def __init__(self, attr):
        self._restrict(attr)
        self._create(attr)

    def _restrict(self, attr):
        raise Exception('サブクラスの責務')

    def _create(self, attr):
        self.__attr = attr

    @property
    def attr(self):
        return self.__attr
