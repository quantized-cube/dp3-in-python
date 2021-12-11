from abc import ABCMeta, abstractmethod


class Entry(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self) -> str:
        # 名前を得る
        pass

    @abstractmethod
    def get_size(self) -> int:
        # サイズを得る
        pass

    @abstractmethod
    def print_list(self, prefix: str = "") -> None:
        # prefixを前につけて一覧を表示する
        pass

    # 文字列表現
    def __str__(self) -> str:
        return f"{self.get_name()} ({self.get_size()})"


class File(Entry):
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size

    def print_list(self, prefix: str = "") -> None:
        print(f"{prefix}/{self}")


class Directory(Entry):
    def __init__(self, name: str) -> None:
        self.name = name
        self.directory: list[Entry] = []

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        size = 0
        for entry in self.directory:
            size += entry.get_size()
        return size

    def print_list(self, prefix: str = "") -> None:
        print(f"{prefix}/{self}")
        for entry in self.directory:
            entry.print_list(f"{prefix}/{self.name}")

    # ディレクトリエントリをディレクトリに追加する
    def add(self, entry: Entry) -> Entry:
        self.directory.append(entry)
        return self


def main() -> None:
    print("Making root entries...")
    rootdir = Directory("root")
    bindir = Directory("bin")
    tmpdir = Directory("tmp")
    usrdir = Directory("usr")
    rootdir.add(bindir)
    rootdir.add(tmpdir)
    rootdir.add(usrdir)
    bindir.add(File("vi", 10000))
    bindir.add(File("latex", 20000))
    rootdir.print_list()
    print()

    print("Making user entries...")
    yuki = Directory("yuki")
    hanako = Directory("hanako")
    tomura = Directory("tomura")
    usrdir.add(yuki)
    usrdir.add(hanako)
    usrdir.add(tomura)
    yuki.add(File("diary.html", 100))
    yuki.add(File("Composite.java", 200))
    hanako.add(File("memo.tex", 300))
    tomura.add(File("game.doc", 400))
    tomura.add(File("junk.mail", 500))
    rootdir.print_list()


if __name__ == "__main__":
    main()
