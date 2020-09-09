import re
from . import attribute


class Sex(attribute.Attribute):
    def _validation_exception(self):
        raise Exception('性別は牡/牝/セのいずれかを指定してください')

    def _validation(self, attr):
        if attr is None:
            return False
        if attr not in ('牡', '牝', 'セ'):
            return False

        return True
