from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Iterator


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self,  file_or_directory: Entry) -> None:
        pass


class Element(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, v: Visitor) -> None:
        pass


class Entry(Element, metaclass=ABCMeta):
    @abstractmethod
    def get_name(self) -> str:
        # 名前を得る
        pass

    @abstractmethod
    def get_size(self) -> int:
        # サイズを得る
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

    def accept(self, v: Visitor) -> None:
        v.visit(self)


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

    def add(self, entry: Entry) -> Entry:
        self.directory.append(entry)
        return self

    def __iter__(self) -> Iterator[Entry]:
        return iter(self.directory)

    def accept(self, v: Visitor) -> None:
        v.visit(self)


class ListVisitor(Visitor):
    def __init__(self) -> None:
        # 現在注目しているディレクトリ名
        self.currentdir = ""

    def visit(self,  file_or_directory: Entry) -> None:
        # File訪問時
        if isinstance(file_or_directory, File):
            print(f"{self.currentdir}/{file_or_directory}")
        elif isinstance(file_or_directory, Directory):
            directory = file_or_directory
            print(f"{self.currentdir}/{directory}")
            savedir = self.currentdir
            self.currentdir = self.currentdir + "/" + directory.get_name()
            for entry in directory:
                entry.accept(self)
            self.currentdir = savedir


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
    rootdir.accept(ListVisitor())
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
    rootdir.accept(ListVisitor())


if __name__ == "__main__":
    main()
