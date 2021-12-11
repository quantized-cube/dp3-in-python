from __future__ import annotations
from abc import ABCMeta, abstractmethod
import random
import time


class Observer(metaclass=ABCMeta):
    @ abstractmethod
    def update(self, generator: NumberGenerator) -> None:
        pass


class NumberGenerator(metaclass=ABCMeta):

    def __init__(self) -> None:
        self.observers: list[Observer] = []

    # Observerを追加する
    def add_observer(self, observer: Observer) -> None:
        self.observers.append(observer)

    # Observerを削除する
    def delete_observer(self, observer: Observer) -> None:
        self.observers.remove(observer)

    # Observerへ通知する
    def notify_observers(self) -> None:
        for o in self.observers:
            o.update(self)

    @ abstractmethod
    def get_number(self) -> int:
        # 数を取得する
        pass

    @ abstractmethod
    def execute(self) -> None:
        # 数を生成する
        pass


class RandomNumberGenerator(NumberGenerator):

    def __init__(self) -> None:
        super().__init__()
        self.number = 0  # 現在の数

    def get_number(self) -> int:
        # 数を取得する
        return self.number

    def execute(self) -> None:
        # 数を生成する
        for _ in range(20):
            self.number = random.randint(0, 49)
            self.notify_observers()


class DigitObserver(Observer):
    def update(self, generator: NumberGenerator) -> None:
        print(f"DigitObserver: {generator.get_number()}")
        try:
            time.sleep(0.1)
        except KeyboardInterrupt as e:
            print(e)


class GraphObserver(Observer):
    def update(self, generator: NumberGenerator) -> None:
        count = generator.get_number()
        print("GraphObserver: " + "*"*count)
        try:
            time.sleep(0.1)
        except KeyboardInterrupt as e:
            print(e)


def main() -> None:
    generator = RandomNumberGenerator()
    observer1 = DigitObserver()
    observer2 = GraphObserver()
    generator.add_observer(observer1)
    generator.add_observer(observer2)
    generator.execute()


if __name__ == "__main__":
    main()
