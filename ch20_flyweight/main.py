from __future__ import annotations
import sys


class BigChar:

    # コンストラクタ
    def __init__(self, charname: str) -> None:
        assert len(charname) == 1
        # 文字の名前
        self._charname = charname
        # 大きな文字を表現する文字列('#' '.' '\n'の列)
        try:
            filename = "text/big" + charname + ".txt"
            with open(filename, "r") as f:
                self._fontdata = f.read()
        except IOError:
            self._fontdata = charname + "?"

    # 大きな文字を表示する
    def print(self) -> None:
        print(self._fontdata, end="")


class BigCharFactory:

    # すでに作ったBigCharのインスタンスを管理
    _pool: dict[str, BigChar] = {}

    # Singletonパターン
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super().__new__(cls, *args, **kwargs)
        return cls._singleton

    # BigCharのインスタンス生成(共有)
    def get_big_char(self, charname: str) -> BigChar:
        assert len(charname) == 1
        bc = self._pool.get(charname)
        if bc is None:
            # ここでBigCharのインスタンスを生成
            bc = BigChar(charname)
            self._pool[charname] = bc
            # print(f'{charname} added to pool.')
        return bc


class BigString:

    # コンストラクタ
    def __init__(self, string: str) -> None:
        factory = BigCharFactory()
        # 「大きな文字」の配列
        bigchars: list[BigChar] = []
        for i in range(len(string)):
            bigchars.append(factory.get_big_char(string[i]))
        self._bigchars = bigchars

    # 表示
    def print(self) -> None:
        for bc in self._bigchars:
            bc.print()


def main(*args: str) -> None:
    if len(args) == 0:
        print("Usage: python main.py digits")
        print("Example: python main.py 1212123")
        sys.exit()

    bs = BigString(args[0])
    bs.print()


if __name__ == "__main__":
    args = sys.argv
    main(*args[1:])
