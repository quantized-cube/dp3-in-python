from pathlib import Path


class HtmlWriter:
    def __init__(self, writer: Path) -> None:
        self.writer = writer
        self.content = ""

    # タイトルの出力
    def title(self, title: str) -> None:
        self.content += "<!DOCTYPE html>"
        self.content += '<html lang="ja">'
        self.content += "<head>"
        self.content += "<title>" + title + "</title>"
        self.content += "</head>"
        self.content += "<body>"
        self.content += "\n"
        self.content += "<h1>" + title + "</h1>"
        self.content += "\n"

    # 段落の出力
    def paragraph(self, msg: str) -> None:
        self.content += "<p>" + msg + "</p>"
        self.content += "\n"

    # リンクの出力
    def link(self, href: str, caption: str) -> None:
        self.paragraph("<a href=\"" + href + "\">" + caption + "</a>")

    # メールアドレスの出力
    def mailto(self, mailaddr: str, username: str) -> None:
        self.link("mailto:" + mailaddr, username)

    # 閉じる
    def close(self) -> None:
        self.content += "</body>"
        self.content += "</html>"
        self.content += "\n"
        with open(self.writer, "w") as f:
            f.write(self.content)
