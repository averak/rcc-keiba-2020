# -*- coding: utf-8 -*-


class Repository:
    def __init__(self):
        self.__container = []

    def store(self, data):
        self._restrict(data)
        self.container.append(data)

    def find(self, key):
        result = []
        for data in self.container:
            if self._is_match(data, key):
                result.append(data)

        return result

    def _restrict(self, data):
        raise Exception('サブクラスの責務')

    def _is_match(self, data, key):
        raise Exception('サブクラスの責務')

    @property
    def container(self):
        return self.__container
