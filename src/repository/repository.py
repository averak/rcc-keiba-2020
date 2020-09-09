class Repository(list):
    def __init__(self, type_):
        self.__type = type_

    def store(self, data):
        if type(data) is not self.__type:
            raise Exception('%sを指定してください' % self.__type)
        self.append(data)

    def find(self, key, attr='id'):
        result = []
        for data in self:
            if not hasattr(data, attr):
                continue

            if key.__eq__(eval('data.%s' % attr)):
                result.append(data)

        return result
