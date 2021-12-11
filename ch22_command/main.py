from __future__ import annotations
import os
import time
from pynput import keyboard
from command import MacroCommand
from drawer import DrawCanvas, DrawCommand


class Main:

    # コンストラクタ
    def __init__(self, title: str) -> None:
        print(f"title: {title}")

        # 描画履歴
        self._history = MacroCommand()
        # 描画領域
        self._canvas = DrawCanvas(400, 400, self._history)
        # 消去ボタン
        self.clear_button = "c"

        self.mouse_dragged = ["a", "s", "d", "q", "w", "e"]
        self.window_closing = "x"
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

        print("valid: a, s, d, q, w, e; ", end="")
        print("c: clear; ", end="")
        print("x: exit")

    def on_press(self, key):
        e = ""
        try:
            e = key.char
            # print('alphanumeric key {0} pressed'.format(e))
        except AttributeError:
            # print('special key {0} pressed'.format(key))
            pass

        if e in self.mouse_dragged:
            cmd = DrawCommand(self._canvas, e)
            self._history.append(cmd)
            cmd.execute()
        elif e == self.clear_button:
            self._history.clear()
            self._canvas.repaint()
        elif e == self.window_closing:
            os._exit(0)
        else:
            pass

    # def __call__(self) -> None:
    #     pass
    #     # Main("Command Pattern Sample")


if __name__ == "__main__":
    main = Main("Command Pattern Sample")
    while True:
        time.sleep(10)
