# -*- coding: utf-8 -*-
from . import model


class Horse(model.Model):
    def _hook_create(self, config):
        self.__name = config['name']
        self.__birthday = config['birthday']
        self.__sex = config['sex']

    @property
    def name(self):
        return self.__name.attr

    @property
    def birthday(self):
        return self.__birthday.attr
