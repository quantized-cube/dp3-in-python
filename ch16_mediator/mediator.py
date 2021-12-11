from abc import ABCMeta, abstractmethod


class Mediator(metaclass=ABCMeta):
    @abstractmethod
    def create_colleagues(self) -> None:
        # Colleagueたちを生成する
        pass

    @abstractmethod
    def colleague_changed(self) -> None:
        # Colleageの状態が変化したときに呼ばれる
        pass
