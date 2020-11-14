from . import attribute
from . import attr_money


class RacePrize(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('レース賞金はMoneyオブジェクトの配列を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) is not list:
            return False
        for money in attr:
            if type(money) is not attr_money.Money:
                return False

        return True

    def __str__(self):
        return ','.join([str(money.attr // 10000) for money in self.attr]) + '万円'
