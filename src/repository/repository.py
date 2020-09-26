import json


class Repository(list):
    files = []
    type_ = None

    def __init__(self):
        self.__read_files()

    def __read_files(self):
        for file_name in self.files:
            with open(file_name) as f:
                rows = json.load(f)

                for row in rows:
                    data = self.__convert_domain(row)
                    self.store(data)

    def __convert_domain(self, data):
        return eval('self.type_(%s)' % ','.join(
            ['%s=\'%s\'' % (key, data[key]) for key in data]))

    def store(self, data):
        if type(data) is not self.type_:
            raise Exception('%sを指定してください' % self.type_)
        if data in self:
            raise Exception('要素が重複しています')

        self.append(data)

    def find(self, key, attr='id'):
        result = []
        for data in self:
            if not hasattr(data, attr):
                continue

            if key.__eq__(eval('data.%s' % attr)):
                result.append(data)

        return result
