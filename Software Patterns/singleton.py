class Singleton(object):
    instance = None

    def __new__(cls, name: str):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self, name: str):
        self.name = name
        pass

    def get_name(self):
        return self.name


# Usage
mySingleton1 = Singleton(name='a')
assert mySingleton1.get_name() == 'a'

mySingleton2 = Singleton(name='b')

# mySingleton1 and mySingleton2 is the same instance, so have the same value as name
assert mySingleton1 is mySingleton2
assert mySingleton1.get_name() == 'b'
assert mySingleton2.get_name() == 'b'

