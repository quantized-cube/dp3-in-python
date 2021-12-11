from __future__ import annotations
from abc import ABCMeta, abstractmethod
import time


class Printable(metaclass=ABCMeta):
    @abstractmethod
    def setPrinterName(self,  name: str) -> None:
        # 名前の設定
        pass

    @abstractmethod
    def getPrinterName(self) -> str:
        # 名前の取得
        pass

    @abstractmethod
    def print(self, string: str) -> None:
        # 文字列表示(プリントアウト)
        pass


class Printer(Printable):

    # コンストラクタ
    def __init__(self, name: str = "") -> None:
        self._name = name  # 名前
        if name:
            # （名前指定）
            self._heavyJob(f"Printerのインスタンス({name})を生成中")
        else:
            self._heavyJob("Printerのインスタンスを生成中")

    # 名前の設定
    def setPrinterName(self, name: str):
        self._name = name

    # 名前の取得
    def getPrinterName(self) -> str:
        return self._name

    # 名前付きで表示
    def print(self, string: str) -> None:
        print(f"=== {self._name} ===")
        print(string)

    # 重い作業(のつもり)
    def _heavyJob(self, msg: str) -> None:
        print(msg, end="", flush=True)
        for _ in range(5):
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                pass
            print(".", end="", flush=True)
        print("完了。")


class PrinterProxy(Printable):

    # コンストラクタ
    def __init__(self, name: str = "No Name") -> None:
        self._name = name  # 名前
        self._real: Printer | None = None  # 「本人」

    # 名前の設定
    def setPrinterName(self, name: str) -> None:
        if self._real:
            # 「本人」にも設定する
            self._real.setPrinterName(name)
        self._name = name

    # 名前の取得
    def getPrinterName(self) -> str:
        return self._name

    # 表示
    def print(self, string: str) -> None:
        self._realize()
        self._real.print(string)

    # 「本人」を生成
    def _realize(self) -> None:
        if self._real is None:
            self._real = Printer(self._name)


def main() -> None:
    p = PrinterProxy("Alice")
    print(f"名前は現在 {p.getPrinterName()}です。")
    p.setPrinterName("Bob")
    print(f"名前は現在 {p.getPrinterName()}です。")
    p.print("Hello, world.")


if __name__ == "__main__":
    main()
