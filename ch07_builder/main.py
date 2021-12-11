from __future__ import annotations
from abc import ABCMeta, abstractmethod
from collections import deque
import sys


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def make_title(self, title: str) -> None:
        pass

    @abstractmethod
    def make_string(self, str_: str) -> None:
        pass

    @abstractmethod
    def make_items(self, items: list[str]) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass


class Director:
    # コンストラクタ
    def __init__(self, builder: Builder) -> None:
        self._builder = builder

    # 文書を作るメソッド
    def construct(self):
        self._builder.make_title("Greeting")
        self._builder.make_string("一般的なあいさつ")
        self._builder.make_items([
            "How are you?",
            "Hello.",
            "Hi.",
        ])
        self._builder.make_string("時間帯に応じたあいさつ")
        self._builder.make_items([
            "Good morning.",
            "Good afternoon.",
            "Good evening.",
        ])
        self._builder.close()


class TextBuilder(Builder):

    def __init__(self) -> None:
        self._sb: deque[str] = deque()

    def make_title(self, title: str) -> None:
        self._sb.append("==============================\n")
        self._sb.append("『")
        self._sb.append(title)
        self._sb.append("』\n\n")

    def make_string(self, str_: str) -> None:
        self._sb.append("■")
        self._sb.append(str_)
        self._sb.append("\n\n")

    def make_items(self, items: list[str]) -> None:
        for s in items:
            self._sb.append("　・")
            self._sb.append(s)
            self._sb.append("\n")
        self._sb.append("\n")

    def close(self) -> None:
        self._sb.append("==============================\n")

    def get_text_result(self) -> str:
        return "".join(self._sb)


class HTMLBuilder(Builder):

    def __init__(self) -> None:
        self._filename = "untitled.html"
        self._sb: deque[str] = deque()

    def make_title(self, title: str) -> None:
        self._filename = title + ".html"
        self._sb.append("<!DOCTYPE html>\n")
        self._sb.append('<html lang="ja">\n')
        self._sb.append("<head><title>")
        self._sb.append(title)
        self._sb.append("</title></head>\n")
        self._sb.append("<body>\n")
        self._sb.append("<h1>")
        self._sb.append(title)
        self._sb.append("</h1>\n\n")

    def make_string(self, str_: str) -> None:
        self._sb.append("<p>")
        self._sb.append(str_)
        self._sb.append("</p>\n\n")

    def make_items(self, items: list[str]) -> None:
        self._sb.append("<ul>\n")
        for s in items:
            self._sb.append("<li>")
            self._sb.append(s)
            self._sb.append("</li>\n")
        self._sb.append("</ul>\n\n")

    def close(self) -> None:
        self._sb.append("</body>")
        self._sb.append("</html>\n")
        with open(self._filename, "w", encoding="utf-8") as f:
            f.write("".join(self._sb))

    def get_HTML_result(self) -> str:
        return self._filename


# 使い方を表示する
def usage() -> None:
    print("Usage: python main.py text       テキストで文書作成")
    print("Usage: python main.py html       HTMLファイルで文書作成")


def main(*args: str) -> None:
    if len(args) != 1:
        usage()
        sys.exit()
    if args[0] == "text":
        textbuilder = TextBuilder()
        director = Director(textbuilder)
        director.construct()
        result = textbuilder.get_text_result()
        print(result)
    elif args[0] == "html":
        htmlbuilder = HTMLBuilder()
        director = Director(htmlbuilder)
        director.construct()
        filename = htmlbuilder.get_HTML_result()
        print(f"HTMLファイル {filename} が作成されました。")
    else:
        usage()
        sys.exit()


if __name__ == "__main__":
    args = sys.argv
    main(*args[1:])
