from . import attribute


class ID(attribute.Attribute):
    id_type = ''
    max_digit = 10

    def _validation_exception(self):
        raise Exception('%sIDは%d桁の文字列を指定してください' %
                        (self.id_type, self.max_digit))

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) is not str:
            return False
        if len(attr) != self.max_digit:
            return False

        return True
