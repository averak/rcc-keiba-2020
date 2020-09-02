# -*- coding: utf-8 -*-
from . import attribute


class Ground(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('馬場状態がNoneです')
        if type(attr) is not int:
            raise Exception('馬場状態は|0: 芝 1: ダート|で指定してください')
        if attr not in [0, 1]:
            raise Exception('馬場状態は|0: 芝 1: ダート|で指定してください')
