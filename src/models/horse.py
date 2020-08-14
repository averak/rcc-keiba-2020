# -*- coding: utf-8 -*-
from . import model


class Horse(model.Model):
    def _hook_create(self, config):
        self.__birthday = config['birthday']
