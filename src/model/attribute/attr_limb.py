from . import attribute


class Limb(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('脚質特性は|0~1 0:逃げ 1:追込|の小数を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) not in (int, float):
            return False
        if attr < 0 or attr > 1:
            return False

        return True
