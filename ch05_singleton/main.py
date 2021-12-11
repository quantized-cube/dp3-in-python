class Singleton1:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            print("インスタンスを生成しました。")
        return cls._instance


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
            print("インスタンスを生成しました。")
        return cls._instances[cls]


class Singleton2(metaclass=MetaSingleton):
    pass


def main1():
    print("Start 1.")
    obj1 = Singleton1()
    obj2 = Singleton1()
    if obj1 == obj2:
        print("obj1とobj2は同じインスタンスです。")
    else:
        print("obj1とobj2は同じインスタンスではありません。")
    if id(obj1) == id(obj2):
        print("obj1とobj2はidも同じです。")
    print("End 1.")


def main2():
    print("Start 2.")
    obj1 = Singleton2()
    obj2 = Singleton2()
    if obj1 == obj2:
        print("obj1とobj2は同じインスタンスです。")
    else:
        print("obj1とobj2は同じインスタンスではありません。")
    if id(obj1) == id(obj2):
        print("obj1とobj2はidも同じです。")
    print("End 2.")


if __name__ == "__main__":
    main1()
    print()
    main2()
