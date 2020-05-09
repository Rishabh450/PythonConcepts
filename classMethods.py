class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

    @staticmethod
    def hey():
        print("No args")


myobject = Foo()
Foo.hi()
Foo.hey()
