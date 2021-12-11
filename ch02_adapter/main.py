from abc import ABCMeta, abstractmethod


# 100VのAC電源、adaptee
class Banner:
    def __init__(self, string: str) -> None:
        self.string = string

    def show_with_paren(self) -> None:
        print(f"({self.string})")

    def show_with_aster(self) -> None:
        print(f"*{self.string}*")


# DC 12V で動くノートパソコン、target
class Print(metaclass=ABCMeta):
    @abstractmethod
    def print_weak(self) -> None:
        pass

    @abstractmethod
    def print_strong(self) -> None:
        pass


# adapter
class PrintBanner(Print):
    def __init__(self, string: str) -> None:
        self.banner = Banner(string)

    def print_weak(self) -> None:
        self.banner.show_with_paren()

    def print_strong(self) -> None:
        self.banner.show_with_aster()


def main() -> None:
    p = PrintBanner("Hello")
    p.print_weak()
    p.print_strong()


if __name__ == "__main__":
    main()
