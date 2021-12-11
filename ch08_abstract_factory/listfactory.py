from __future__ import annotations
from factory import Factory, Link, Page, Tray


class ListLink(Link):
    def __init__(self, caption: str, url: str) -> None:
        super().__init__(caption, url)

    def make_HTML(self) -> str:
        return "  <li><a href=\"" + self.url + "\">" + self.caption + "</a></li>\n"


class ListTray(Tray):

    def __init__(self, caption: str) -> None:
        super().__init__(caption)
        self.caption = caption

    def make_HTML(self) -> str:
        sb = []
        sb.append("<li>\n")
        sb.append(self.caption)
        sb.append("\n<ul>\n")
        for item in self.tray:
            sb.append(item.make_HTML())
        sb.append("</ul>\n")
        sb.append("</li>\n")
        return "".join(sb)


class ListPage(Page):
    def __init__(self, title: str, author: str) -> None:
        super().__init__(title, author)

    def make_HTML(self) -> str:
        sb = []
        sb.append("<!DOCTYPE html>\n")
        sb.append('<html lang="ja"><head><title>')
        sb.append(self.title)
        sb.append("</title></head>\n")
        sb.append("<body>\n")
        sb.append("<h1>")
        sb.append(self.title)
        sb.append("</h1>\n")
        sb.append("<ul>\n")
        for item in self.content:
            sb.append(item.make_HTML())
        sb.append("</ul>\n")
        sb.append("<hr><address>")
        sb.append(self.author)
        sb.append("</address>\n")
        sb.append("</body></html>\n")
        return "".join(sb)


class ListFactory(Factory):

    def create_link(self, caption: str,  url: str) -> Link:
        return ListLink(caption, url)

    def create_tray(self, caption: str) -> Tray:
        return ListTray(caption)

    def create_page(self, title: str,  author: str) -> Page:
        return ListPage(title, author)
