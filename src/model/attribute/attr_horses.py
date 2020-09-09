from . import attribute
import model


class Horses(attribute.Attribute):
    max_size = 21

    def _validation_exception(self):
        raise Exception('出場馬一覧は長さ%d以下のHorseオブジェクトの配列を指定してください' % self.max_size)

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) is not list:
            return False
        for horse in attr:
            if type(horse) is not model.Horse:
                return False
        if len(attr) > self.max_size:
            return False

        return True

    @property
    def n_horses(self):
        return len(self.attr)
