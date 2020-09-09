from . import attribute
import model

class Horses(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('出場馬一覧はHorseオブジェクトの配列を指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) is not list:
            return False
        for horse in attr:
            if type(horse) is not model.Horse:
                return False

        return True

    @property
    def n_horses(self):
        return len(self.attr)
