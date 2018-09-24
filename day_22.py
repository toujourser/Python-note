class Property:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        # print(instance)
        return self.fget(instance)

    def __set__(self, instance, value):
        # print('2', self.fget, self.fset, value)
        self.fset(instance, value)

    def setter(self, fn):
        # print('1', self.fget, self.fset, fn)
        self.fset = fn
        return self


class A:
    def __init__(self, data):
        self._data = data

    @Property  # data = Property(data) => data = Property实例
    def data(self):
        print(self._data)

    @data.setter  # data = data.setter(data) => data = Property(data).setter(data) =>  data = Property实例.setter(data)
    def data(self, value):
        self._data = value


a = A('abc')
a.data
a.data = 'xyz'
a.data
