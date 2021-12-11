from __future__ import annotations
from enum import Enum, unique


@unique
class Hand(Enum):

    # じゃんけんの手を表す3つのenum定数
    ROCK = 0  # "グー"
    SCISSORS = 1  # "チョキ"
    PAPER = 2  # "パー"

    @classmethod
    def get_hand(cls, handvalue: int) -> Hand:
        # 手の値からenum定数を得る
        return Hand(handvalue)

    # selfがhより強いときTrue
    def isStrongerThan(self, h: Hand) -> bool:
        return self._fight(h) == 1

    # selfがhより弱いときTrue
    def isWeakerThan(self, h: Hand) -> bool:
        return self._fight(h) == -1

    # 引き分けは0, selfの勝ちなら1, hの勝ちなら-1
    def _fight(self, h: Hand) -> int:
        if (self == h):
            return 0
        elif ((self.value + 1) % 3 == h.value):
            return 1
        else:
            return -1

    # じゃんけんの「手」の文字列表現
    def __str__(self):
        if self is Hand.ROCK:
            return "グー"
        elif self is Hand.SCISSORS:
            return "チョキ"
        else:
            return "パー"
