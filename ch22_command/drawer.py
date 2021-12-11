from __future__ import annotations
from abc import ABCMeta, abstractmethod
from command import Command, MacroCommand


Point = str


class DrawCommand(Command):

    # コンストラクタ
    def __init__(self, drawable: Drawable, position: Point) -> None:
        self.drawable = drawable  # 描画対象
        self._position = position  # 描画位置

    # 実行
    def execute(self) -> None:
        self.drawable.draw(self._position)

    def __str__(self) -> str:
        return self._position


class Drawable(metaclass=ABCMeta):
    @abstractmethod
    def draw(self, x: str) -> None:
        # 位置の代わりに文字を入力
        pass


class DrawCanvas(Drawable):

    # コンストラクタ
    def __init__(self, width: int, height: int, history: MacroCommand) -> None:
        print(f"set size to {width}, {height}")
        print("set background color to white")
        self._color = "red"  # 描画色
        self._radius = 6  # 描画する点の半径
        self._history = history  # 履歴

    # 履歴全体を再描画
    def paint(self) -> None:
        self._history.execute()

    # 描画
    def draw(self, x: str) -> None:
        # print(f"set color to {self._color}")
        # print(x)
        print(self._history)

    def repaint(self) -> None:
        print("repaint")
