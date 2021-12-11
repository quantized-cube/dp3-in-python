from __future__ import annotations
from abc import ABCMeta, abstractmethod
import os
import time
from pynput import keyboard


class State(metaclass=ABCMeta):
    @ abstractmethod
    def doClock(self, context: Context, hour: int) -> None:
        # 時刻設定
        pass

    @ abstractmethod
    def doUse(self, context: Context) -> None:
        # 金庫使用
        pass

    @ abstractmethod
    def doAlarm(self, context: Context) -> None:
        # 非常ベル
        pass

    @ abstractmethod
    def doPhone(self, context: Context) -> None:
        # 通常通話
        pass


class DayState(State):

    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super().__new__(cls, *args, **kwargs)
        return cls._singleton

    def doClock(self, context: Context, hour: int) -> None:
        if (hour < 9) | (17 <= hour):
            context.changeState(NightState())

    def doUse(self, context: Context) -> None:
        context.recordLog("金庫使用(昼間)")

    def doAlarm(self, context: Context) -> None:
        context.callSecurityCenter("非常ベル(昼間)")

    def doPhone(self, context: Context) -> None:
        context.callSecurityCenter("通常の通話(昼間)")

    def __str__(self) -> str:
        return "[昼間]"


class NightState(State):

    _singleton = None

    def __new__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = super().__new__(cls, *args, **kwargs)
        return cls._singleton

    def doClock(self, context: Context, hour: int) -> None:
        if (9 <= hour) & (hour < 17):
            context.changeState(DayState())

    def doUse(self, context: Context) -> None:
        context.callSecurityCenter("非常：夜間の金庫使用！")

    def doAlarm(self, context: Context) -> None:
        context.callSecurityCenter("非常ベル(夜間)")

    def doPhone(self, context: Context) -> None:
        context.recordLog("夜間の通話録音")

    def __str__(self) -> str:
        return "[夜間]"


class Context(metaclass=ABCMeta):
    @ abstractmethod
    def setClock(self, hour: int) -> None:
        # 時刻の設定
        pass

    @ abstractmethod
    def changeState(self, state: State) -> None:
        # 状態変化
        pass

    @ abstractmethod
    def callSecurityCenter(self, msg: str) -> None:
        # 警備センター警備員呼び出し
        pass

    @ abstractmethod
    def recordLog(self, msg: str) -> None:
        # 警備センター記録
        pass


Button = str


class SafeFrame(Context):

    def __init__(self, title: str) -> None:
        self._buttonUse: Button = "a"    # 金庫使用ボタン
        self._buttonAlarm: Button = "s"  # 非常ベルボタン
        self._buttonPhone: Button = "d"  # 通常通話ボタン
        self._buttonExit: Button = "f"   # 終了ボタン

        self._state: State = DayState()  # 現在の状態

        print(f"[title: {title}]")
        print("a: 金庫使用, ", end="")
        print("s: 非常ベル, ", end="")
        print("d: 通常通話, ", end="")
        print("f: 終了")

        # リスナーの設定
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()

    # ボタンが押されたらここに来る
    def on_press(self, key):
        e = ""
        try:
            e = key.char
            print('alphanumeric key {0} pressed'.format(e))
        except AttributeError:
            print('special key {0} pressed'.format(key))

        if e == self._buttonUse:  # 金庫使用ボタン
            self._state.doUse(self)
        elif e == self._buttonAlarm:  # 非常ベルボタン
            self._state.doAlarm(self)
        elif e == self._buttonPhone:  # 通常通話ボタン
            self._state.doPhone(self)
        elif e == self._buttonExit:  # 終了ボタン
            os._exit(0)
        else:
            print("?")

    # 時刻の設定
    def setClock(self, hour: int) -> None:
        clockstring = f"現在時刻は{hour:0>2}:00"
        print(clockstring)
        self._state.doClock(self, hour)

    # 状態変化
    def changeState(self, state: State) -> None:
        print(f"{self._state}から{state}へ状態が変化しました。")
        self._state = state

    # 警備センター警備員呼び出し
    def callSecurityCenter(self, msg: str) -> None:
        print("call! " + msg)

    # 警備センター記録
    def recordLog(self, msg: str) -> None:
        print("record ... " + msg)


def main() -> None:
    frame = SafeFrame("State Sample")
    while True:
        for hour in range(0, 24):
            frame.setClock(hour)   # 時刻の設定
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                pass


if __name__ == "__main__":
    main()
