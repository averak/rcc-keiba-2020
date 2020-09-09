from . import attribute


class Ground(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('馬場状態は芝/ダートのいずれかを指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if attr not in ('芝', 'ダート'):
            return False

        return True
