from . import attribute


class Turn(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('周回方向は右/左のいずれかを指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if attr not in ('右', '左'):
            return False

        return True
