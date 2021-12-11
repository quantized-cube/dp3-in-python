from __future__ import annotations
from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self, s: str) -> None:
        pass

    @abstractmethod
    def create_copy(self) -> Product:
        pass


class Manager:
    _showcase: dict[str, Product] = {}

    @classmethod
    def register(cls, name: str, prototype: Product) -> None:
        cls._showcase[name] = prototype

    @classmethod
    def create(cls, prototype_name: str) -> Product:
        p = cls._showcase[prototype_name]
        return p.create_copy()
