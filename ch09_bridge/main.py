from abc import ABCMeta, abstractmethod
from typing import final


class DisplayImpl(metaclass=ABCMeta):
    @abstractmethod
    def rawOpen(self) -> None:
        pass

    @abstractmethod
    def rawPrint(self) -> None:
        pass

    @abstractmethod
    def rawClose(self) -> None:
        pass


class Display:
    def __init__(self, impl: DisplayImpl) -> None:
        self._impl = impl

    def open(self) -> None:
        self._impl.rawOpen()

    def print(self) -> None:
        self._impl.rawPrint()

    def close(self) -> None:
        self._impl.rawClose()

    @final
    def display(self) -> None:
        self.open()
        self.print()
        self.close()


class CountDisplay(Display):
    def __init__(self, impl: DisplayImpl) -> None:
        super().__init__(impl)

    def multiDisplay(self, times: int) -> None:
        self.open()
        for _ in range(times):
            self.print()
        self.close()


class StringDisplayImpl(DisplayImpl):
    def __init__(self, string: str) -> None:
        self._string = string
        self._width = len(string)

    def rawOpen(self) -> None:
        self._printLine()

    def rawPrint(self) -> None:
        print("|" + self._string + "|")

    def rawClose(self) -> None:
        self._printLine()

    def _printLine(self) -> None:
        print("+" + "-" * self._width + "+")


def main() -> None:
    d1 = Display(StringDisplayImpl("Hello, Japan."))
    d2 = CountDisplay(StringDisplayImpl("Hello, World."))
    d3 = CountDisplay(StringDisplayImpl("Hello, Universe."))
    d1.display()
    d2.display()
    d3.display()
    d3.multiDisplay(5)


if __name__ == "__main__":
    main()
