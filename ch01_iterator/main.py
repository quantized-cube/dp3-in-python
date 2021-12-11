from collections.abc import Iterable, Iterator


class Book:
    def __init__(self, name: str) -> None:
        self.name = name


class BookShelf(Iterable):
    def __init__(self, maxsize: int) -> None:
        self._books: list[Book] = [Book("")] * maxsize
        self._last = 0

    def get_book_at(self, index: int) -> Book:
        return self._books[index]

    def append_book(self, book: Book) -> None:
        self._books[self._last] = book
        self._last += 1

    def get_length(self) -> int:
        return self._last

    def __iter__(self) -> Iterator[Book]:
        return BookShelfIterator(self)


class BookShelfIterator(Iterator):
    def __init__(self, book_shelf: BookShelf) -> None:
        self._book_shelf = book_shelf
        self._index = 0

    def _has_next(self) -> bool:
        if self._index < self._book_shelf.get_length():
            return True
        else:
            return False

    def __next__(self) -> Book:
        if not self._has_next():
            raise StopIteration()
        book = self._book_shelf.get_book_at(self._index)
        self._index += 1
        return book


def main() -> None:

    book_shelf = BookShelf(4)
    book_shelf.append_book(Book("Around the World in 80 Days"))
    book_shelf.append_book(Book("Bible"))
    book_shelf.append_book(Book("Cinderella"))
    book_shelf.append_book(Book("Daddy-Long-Legs"))

    # 明示的にIteratorを使う方法
    it = book_shelf.__iter__()
    while True:
        try:
            book = next(it)
        except StopIteration:
            break
        print(book.name)
    print()

    # for文を使う方法
    for book in book_shelf:
        print(book.name)
    print()


if __name__ == "__main__":
    main()
