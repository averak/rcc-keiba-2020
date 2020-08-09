# -*- coding: utf-8 -*-


class Horse:
    def __init__(self, id_=None, name=None):
        self.__id = id_
        self.__name = name

    def get_id(self):
        return self.__id.get_attr()

    def get_name(self):
        return self.__name.get_attr()
