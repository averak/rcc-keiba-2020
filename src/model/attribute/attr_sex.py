# -*- coding: utf-8 -*-
import re
from . import attribute


class Sex(attribute.Attribute):
    def _restrict(self, attr):
        if attr is None:
            raise Exception('性別がNoneです')
        if type(attr) is not str:
            raise Exception('性別は牡/牝/セのいずれかを指定してください')
        if len(attr) != 1 or attr not in '牡牝セ':
            raise Exception('性別は牡/牝/セのいずれかを指定してください')
