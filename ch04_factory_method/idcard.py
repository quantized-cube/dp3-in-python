from framework import Factory, Product


class IDCard(Product):
    def __init__(self, owner: str) -> None:
        print(f"{owner}のカードを作ります。")
        self.owner = owner

    def use(self) -> None:
        print(f"{self}を使います。")

    def __str__(self) -> str:
        return f"[IDCard: {self.owner}]"

    def getOwner(self) -> str:
        return self.owner


class IDCardFactory(Factory):
    def createProduct(self, owner: str) -> Product:
        return IDCard(owner)

    def registerProduct(self, product: Product) -> None:
        print(f"{product}を登録しました。")
