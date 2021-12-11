from abc import ABCMeta, abstractmethod


class Display(metaclass=ABCMeta):
    @abstractmethod
    def get_columns(self) -> int:
        # 横の文字数を得る
        pass

    @abstractmethod
    def get_rows(self) -> int:
        # 縦の行数を得る
        pass

    @abstractmethod
    def get_row_text(self,  row: int) -> str:
        # row行目の文字列を得る
        pass

    # すべての行を表示する
    def show(self) -> None:
        for i in range(self.get_rows()):
            print(self.get_row_text(i))


class StringDisplay(Display):
    def __init__(self, string: str) -> None:
        self.string = string  # 表示文字列

    def get_columns(self) -> int:
        return len(self.string)

    def get_rows(self) -> int:
        return 1

    def get_row_text(self,  row: int) -> str:
        if row != 0:
            raise IndexError()
        return self.string


class Border(Display, metaclass=ABCMeta):
    def __init__(self, display: Display) -> None:
        # インスタンス生成時に「中身」を引数で指定
        self.display = display  # この飾り枠がくるんでいる「中身」


class SideBorder(Border):
    def __init__(self, display: Display, ch: str) -> None:
        # 中身となるDisplayと飾り文字を指定
        assert len(ch) == 1
        super().__init__(display)
        self.borderChar = ch

    def get_columns(self) -> int:
        # 文字数は中身の両側に飾り文字分を加えたもの
        return 1 + self.display.get_columns() + 1

    def get_rows(self) -> int:
        # 行数は中身の行数に同じ
        return self.display.get_rows()

    def get_row_text(self,  row: int) -> str:
        # 指定行の内容は、中身の指定行の両側に飾り文字をつけたもの
        return self.borderChar + self.display.get_row_text(row) + self.borderChar


class FullBorder(Border):
    def __init__(self, display: Display) -> None:
        super().__init__(display)

    def get_columns(self) -> int:
        # 文字数は中身の両側に左右の飾り文字分を加えたもの
        return 1 + self.display.get_columns() + 1

    def get_rows(self) -> int:
        # 行数は中身の行数に上下の飾り文字分を加えたもの
        return 1 + self.display.get_rows() + 1

    def get_row_text(self,  row: int) -> str:
        if row == 0:  # 上端の枠
            return "+" + self._make_line('-', self.display.get_columns()) + "+"
        elif row == self.display.get_rows() + 1:  # 下端の枠
            return "+" + self._make_line('-', self.display.get_columns()) + "+"
        else:  # それ以外
            return "|" + self.display.get_row_text(row - 1) + "|"

    # 文字chをcount個連続させた文字列を作る
    def _make_line(self, ch: str,  count: int) -> str:
        assert len(ch) == 1
        return ch*count


def main() -> None:
    b1 = StringDisplay("Hello, world.")
    b2 = SideBorder(b1, '#')
    b3 = FullBorder(b2)
    b1.show()
    b2.show()
    b3.show()
    b4 = SideBorder(
        FullBorder(
            FullBorder(
                SideBorder(
                    FullBorder(
                        StringDisplay("Hello, world.")
                    ),
                    '*'
                )
            )
        ),
        '/'
    )
    b4.show()


if __name__ == "__main__":
    main()
