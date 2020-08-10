# -*- coding: utf-8 -*-
from . import model


class Horse(model.Model):
    def _post_init(self, args):
        self.__birthday = args['birthday']
