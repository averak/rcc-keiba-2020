# -*- coding: utf-8 -*-


class Model:
    def __init__(self, args):
        self.__id = args['id']
        self.__name = args['name']

        self._post_init(args)

    def _post_init(self, args):
        raise Exception('サブクラスの責務')

    @property
    def id(self):
        return self.__id.attr

    @property
    def name(self):
        return self.__name.attr
