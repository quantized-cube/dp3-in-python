from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Item(metaclass=ABCMeta):
    def __init__(self, caption: str) -> None:
        self.caption = caption

    @abstractmethod
    def make_HTML(self) -> str:
        pass


class Link(Item, metaclass=ABCMeta):
    def __init__(self, caption: str, url: str) -> None:
        super().__init__(caption)
        self.url = url


class Tray(Item, metaclass=ABCMeta):

    def __init__(self, caption: str) -> None:
        super().__init__(caption)
        self.tray: list[Item] = []

    def add(self, item: Item) -> None:
        self.tray.append(item)


class Page(metaclass=ABCMeta):
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.content: list[Item] = []

    def add(self, item: Item) -> None:
        self.content.append(item)

    def output(self, filename: str) -> None:
        with open(filename, "w") as f:
            f.write(self.make_HTML())
        print(filename + " を作成しました。")

    @abstractmethod
    def make_HTML(self) -> str:
        pass


class Factory(metaclass=ABCMeta):
    @classmethod
    def getFactory(cls, classname: str) -> Factory:
        factory: Factory
        if classname == "listfactory.ListFactory":
            from listfactory import ListFactory
            factory = ListFactory()
        elif classname == "divfactory.DivFactory":
            from divfactory import DivFactory
            factory = DivFactory()
        else:
            raise ValueError("クラス " + classname + " が見つかりません。")
        return factory

    @abstractmethod
    def create_link(self, caption: str,  url: str) -> Link:
        pass

    @abstractmethod
    def create_tray(self, caption: str) -> Tray:
        pass

    @abstractmethod
    def create_page(self, title: str,  author: str) -> Page:
        pass
