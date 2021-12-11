from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Trouble:
    # トラブルの生成
    def __init__(self, number: int) -> None:
        self.number = number  # トラブル番号

    # トラブルの文字列表現
    def __str__(self) -> str:
        return f"[Trouble {self.number}]"


class Support(metaclass=ABCMeta):
    def __init__(self, name: str) -> None:
        self.name = name  # このトラブル解決者の名前
        self.next_: Support | None = None  # たらい回しの先

    # たらい回しの先を設定する
    def set_next(self, next_: Support) -> Support:
        self.next_ = next_
        return next_

    # トラブル解決の手順を定める
    def support(self, trouble: Trouble) -> None:
        if self.resolve(trouble):
            self.done(trouble)
        elif self.next_ is not None:
            self.next_.support(trouble)
        else:
            self.fail(trouble)

    # トラブル解決者の文字列表現
    def __str__(self) -> str:
        return f"[{self.name}]"

    @ abstractmethod
    def resolve(self, trouble: Trouble) -> bool:
        # 解決しようとする
        pass

    # 解決した
    def done(self, trouble: Trouble) -> None:
        print(f"{trouble} is resolved by {self}.")

    # 解決しなかった
    def fail(self, trouble: Trouble) -> None:
        print(f"{trouble} cannot be resolved.")


class NoSupport(Support):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def resolve(self, trouble: Trouble) -> bool:
        return False  # 自分は何も解決しない


class LimitSupport(Support):
    def __init__(self, name: str, limit: int) -> None:
        super().__init__(name)
        self.limit = limit  # この番号未満なら解決できる

    def resolve(self, trouble: Trouble) -> bool:
        if trouble.number < self.limit:
            return True
        else:
            return False


class OddSupport(Support):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def resolve(self, trouble: Trouble) -> bool:
        if trouble.number % 2 == 1:
            return True
        else:
            return False


class SpecialSupport(Support):
    def __init__(self, name: str, number: int) -> None:
        super().__init__(name)
        self.number = number  # この番号だけ解決できる

    def resolve(self, trouble: Trouble) -> bool:
        if trouble.number == self.number:
            return True
        else:
            return False


def main() -> None:
    alice = NoSupport("Alice")
    bob = LimitSupport("Bob", 100)
    charlie = SpecialSupport("Charlie", 429)
    diana = LimitSupport("Diana", 200)
    elmo = OddSupport("Elmo")
    fred = LimitSupport("Fred", 300)

    # 連鎖の形成
    (alice
     .set_next(bob)
     .set_next(charlie)
     .set_next(diana)
     .set_next(elmo)
     .set_next(fred))

    # さまざまなトラブル発生
    for i in range(0, 500, 33):
        alice.support(Trouble(i))


if __name__ == "__main__":
    main()
