from abc import ABCMeta, abstractmethod
from typing import final


class AbstractDisplay(metaclass=ABCMeta):
    # open, print, closeはサブクラスに実装をまかせる抽象メソッド
    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def print(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    # displayはAbstractDisplayで実装してるメソッド
    @final
    def display(self) -> None:
        self.open()
        for _ in range(5):
            self.print()
        self.close()


class CharDisplay(AbstractDisplay):
    def __init__(self, ch: str) -> None:
        assert len(ch) == 1
        self.ch = ch

    def open(self) -> None:
        # 開始文字列として"<<"を表示する
        print("<<", end="")

    def print(self) -> None:
        # フィールドに保存しておいた文字を1回表示する
        print(self.ch, end="")

    def close(self) -> None:
        # 終了文字列として">>"を表示する
        print(">>")


class StringDisplay(AbstractDisplay):
    def __init__(self, string: str) -> None:
        self.string = string
        self.width = len(string)

    def open(self) -> None:
        self._printLine()

    def print(self) -> None:
        print("|"+self.string+"|")

    def close(self) -> None:
        self._printLine()

    # openとcloseから呼び出されて"+----+"という文字列を表示するメソッド
    def _printLine(self) -> None:
        print("+" + "-" * self.width + "+")


def main() -> None:
    # 'H'を持ったCharDisplayのインスタンスを1個作る
    d1 = CharDisplay('H')
    # "Hello, world."を持ったStringDisplayのインスタンスを1個作る
    d2 = StringDisplay("Hello, world.")

    # d1,d2とも、すべて同じAbstractDisplayのサブクラスのインスタンスだから
    # 継承したdisplayメソッドを呼び出すことができる
    # 実際の動作は個々のクラスCharDisplayやStringDisplayで定まる
    d1.display()
    d2.display()


if __name__ == "__main__":
    main()
