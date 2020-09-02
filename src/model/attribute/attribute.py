# -*- coding: utf-8 -*-


class Attribute:
    def __init__(self, attr):
        if not self._validation(attr):
            self._validation_exception()
        self._create(attr)

    def _validation(self, attr):
        raise Exception('サブクラスの責務')

    def _validation_exception(self):
        raise Exception('サブクラスの責務')

    def _create(self, attr):
        self.__attr = attr

    @property
    def attr(self):
        return self.__attr
