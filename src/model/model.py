class Model:
    def __init__(self, **config):
        self.__id = config['id_']

        self._hook_create(config)

    def _hook_create(self, config):
        raise Exception('サブクラスの責務')

    @property
    def id(self):
        return self.__id

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        if self.id.__eq__(other.id):
            return True

        return False
