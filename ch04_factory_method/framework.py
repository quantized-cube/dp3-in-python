from abc import ABCMeta, abstractmethod
from typing import final


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self) -> None:
        pass


class Factory(metaclass=ABCMeta):
    @final
    def create(self, owner: str) -> Product:
        p = self.createProduct(owner)
        self.registerProduct(p)
        return p

    @abstractmethod
    def createProduct(self, owner: str) -> Product:
        pass

    @abstractmethod
    def registerProduct(self, product: Product) -> None:
        pass
