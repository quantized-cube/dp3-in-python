from copy import copy
from framework import Manager, Product


class MessageBox(Product):

    def __init__(self, decochar: str) -> None:
        assert len(decochar) == 1
        self._decochar = decochar

    def use(self, s: str) -> None:
        decolen = 1 + len(s) + 1
        print(self._decochar * decolen)
        print(f"{self._decochar}{s}{self._decochar}")
        print(self._decochar * decolen)

    def create_copy(self) -> Product:
        return copy(self)


class UnderlinePen(Product):

    def __init__(self, ulchar: str) -> None:
        assert len(ulchar) == 1
        self._ulchar = ulchar

    def use(self, s: str) -> None:
        ulen = len(s)
        print(s)
        print(self._ulchar * ulen)

    def create_copy(self) -> Product:
        return copy(self)


def main() -> None:
    # 準備
    manager = Manager()
    upen = UnderlinePen('-')
    mbox = MessageBox('*')
    sbox = MessageBox('/')

    # 登録
    manager.register("strong message", upen)
    manager.register("warning box", mbox)
    manager.register("slash box", sbox)

    # 生成と使用
    p1 = manager.create("strong message")
    p1.use("Hello, world.")

    p2 = manager.create("warning box")
    p2.use("Hello, world.")

    p3 = manager.create("slash box")
    p3.use("Hello, world.")


if __name__ == "__main__":
    main()
