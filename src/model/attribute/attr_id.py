from . import attribute


class ID(attribute.Attribute):
    id_type = ''
    max_digit = 10

    def _validation_exception(self):
        raise Exception('%sIDは%d桁の整数を指定してください' %
                        (self.id_type, self.max_digit))

    def _validation(self, attr):
        if attr is None:
            return False
        if type(attr) is not int:
            return False
        if attr < 0 or len(str(attr)) > self.max_digit:
            return False

        return True

    def __str__(self):
        return str(self.attr).zfill(self.max_digit)
