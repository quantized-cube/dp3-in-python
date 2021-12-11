from __future__ import annotations
from abc import ABCMeta, abstractmethod
import random

from Hand import Hand


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def next_hand(self) -> Hand:
        pass

    @abstractmethod
    def study(self, win: bool) -> None:
        pass


class WinningStrategy(Strategy):
    def __init__(self, seed: int) -> None:
        random.seed(seed)
        self._won = False
        self._prev_hand: Hand

    def next_hand(self) -> Hand:
        if not self._won:
            self._prev_hand = Hand.get_hand(random.randint(0, 2))

        return self._prev_hand

    def study(self, win: bool) -> None:
        self._won = win


class ProbStrategy(Strategy):
    def __init__(self, seed: int) -> None:
        random.seed(seed)
        self._prev_hand_value = 0
        self._current_hand_value = 0
        self._history = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    def next_hand(self) -> Hand:
        bet = random.randint(
            0, self._get_sum(self._current_hand_value) - 1)
        handvalue = 0
        c0 = self._history[self._current_hand_value][0]
        c1 = self._history[self._current_hand_value][1]
        if bet < c0:
            handvalue = 0
        elif bet < c0 + c1:
            handvalue = 1
        else:
            handvalue = 2

        self._prev_hand_value = self._current_hand_value
        self._current_hand_value = handvalue
        return Hand.get_hand(handvalue)

    def _get_sum(self, handvalue: int) -> int:
        sum_ = 0
        for i in range(3):
            sum_ += self._history[handvalue][i]
        return sum_

    def study(self, win: bool) -> None:
        if win:
            self._history[self._prev_hand_value][
                self._current_hand_value] += 1
        else:
            self._history[self._prev_hand_value][(
                self._current_hand_value + 1) % 3] += 1
            self._history[self._prev_hand_value][(
                self._current_hand_value + 2) % 3] += 1
