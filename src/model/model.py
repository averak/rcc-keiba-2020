# -*- coding: utf-8 -*-


class Model:
    def __init__(self, **config):
        self.__id = config['id_']

        self._hook_create(config)

    def _hook_create(self, config):
        raise Exception('サブクラスの責務')

    def equals(self, model):
        return self.id == model.id and type(self) == type(model)

    @property
    def id(self):
        return self.__id.attr
