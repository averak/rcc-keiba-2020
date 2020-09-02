# -*- coding: utf-8 -*-
from . import attribute
from . import attr_id


class PedID(attr_id.ID):
    def _validation_exception(self):
        raise Exception('血統IDは0以上の整数を指定してください')
