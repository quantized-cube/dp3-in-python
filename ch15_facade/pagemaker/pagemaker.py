from pathlib import Path
from .database import get_properties
from .htmlwriter import HtmlWriter


def make_welcome_page(mailaddr: str, filename: str) -> None:
    try:
        mailprop = get_properties("maildata")
        username = mailprop[mailaddr]
        writer = HtmlWriter(Path(filename))
        writer.title(username + "'s web page")
        writer.paragraph("Welcome to " + username + "'s web page!")
        writer.paragraph("Nice to meet you!")
        writer.mailto(mailaddr, username)
        writer.close()
        print(filename + " is created for " + mailaddr + " (" + username + ")")
    except Exception as e:
        print(e)
