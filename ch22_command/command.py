from __future__ import annotations
from abc import ABCMeta, abstractmethod
from collections import deque


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self) -> None:
        pass


class MacroCommand(Command):

    def __init__(self) -> None:
        self._commands: deque[Command] = deque()  # 命令の列

    # 実行
    def execute(self) -> None:
        for cmd in self._commands:
            cmd.execute()

    # 追加
    def append(self, cmd: Command) -> None:
        if cmd == self:
            raise ValueError("infinite loop caused by append")
        self._commands.append(cmd)

    # 最後の命令を削除
    def undo(self) -> None:
        if len(self._commands) != 0:
            self._commands.pop()

    # 全部削除
    def clear(self) -> None:
        self._commands.clear()

    def __str__(self) -> str:
        return "".join(map(str, self._commands))
