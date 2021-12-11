from __future__ import annotations
from Hand import Hand
from Strategy import Strategy


class Player:
    # 名前と戦略を授けてプレイヤーを作る
    def __init__(self, name: str, strategy: Strategy) -> None:
        self.name = name
        self.strategy = strategy
        self.wincount = 0
        self.losecount = 0
        self.gamecount = 0

    # 戦略におうかがいを立てて次の手を決める
    def next_hand(self) -> Hand:
        return self.strategy.next_hand()

    # 勝った
    def win(self) -> None:
        self.strategy.study(True)
        self.wincount += 1
        self.gamecount += 1

    # 負けた
    def lose(self) -> None:
        self.strategy.study(False)
        self.losecount += 1
        self.gamecount += 1

    # 引き分け
    def even(self) -> None:
        self.gamecount += 1

    def __str__(self) -> str:
        return f"[{self.name}: {self.gamecount} games, {self.wincount} win, {self.losecount} lose]"
