import random
import time


Fruit = str
Fruits = list[Fruit]


class Memento:

    # コンストラクタ(wide interface)
    def __init__(self, money: int) -> None:
        self._money = money  # 所持金
        self._fruits: Fruits = []  # フルーツ

    # 所持金を得る(narrow interface)
    def get_money(self) -> int:
        return self._money

    # フルーツを追加する(wide interface)
    def _add_fruit(self, fruit: Fruit) -> None:
        self._fruits.append(fruit)

    # フルーツを得る(wide interface)
    def _get_fruits(self) -> Fruits:
        return self._fruits


class Gamer:

    # フルーツ名の表
    _fruits_name: Fruits = ["リンゴ", "ぶどう", "バナナ", "みかん"]

    # コンストラクタ
    def __init__(self, money: int) -> None:
        # 所持金
        self._money = money
        # フルーツ
        self._fruits: Fruits = []

    # 現在の所持金を得る
    def get_money(self) -> int:
        return self._money

    # 賭ける…ゲームの進行
    def bet(self) -> None:
        # サイコロを振る
        dice = random.randint(1, 6)
        if dice == 1:
            # 1の目…所持金が増える
            self._money += 100
            print("所持金が増えました。")
        elif dice == 2:
            # 2の目…所持金が半分になる
            self._money //= 2
            print("所持金が半分になりました。")
        elif dice == 6:
            # 6の目…フルーツをもらう
            f = self._get_fruit()
            print("フルーツ(" + f + ")をもらいました。")
            self._fruits.append(f)
        else:
            # それ以外…何も起きない
            print("何も起こりませんでした。")

    # スナップショットをとる
    def create_memento(self) -> Memento:
        m = Memento(self._money)
        for f in self._fruits:
            # フルーツはおいしいものだけ保存
            if f.startswith("おいしい"):
                m._add_fruit(f)
        return m

    # アンドゥを行う
    def restore_memento(self, memento: Memento) -> None:
        self._money = memento.get_money()
        self._fruits = memento._get_fruits()

    def __str__(self) -> str:
        return f"[money = {self._money}, fruits = {self._fruits}]"

    # フルーツを1個得る
    def _get_fruit(self) -> str:
        f = Gamer._fruits_name[
            random.randint(0, len(Gamer._fruits_name) - 1)]
        if random.randint(0, 1):
            return "おいしい" + f
        else:
            return f


def main() -> None:
    gamer = Gamer(100)               # 最初の所持金は100
    memento = gamer.create_memento()    # 最初の状態を保存しておく

    # ゲームスタート
    for i in range(100):
        print(f"==== {i}")        # 回数表示
        print(f"現状:{gamer}")    # 現在の主人公の状態表示

        # ゲームを進める
        gamer.bet()

        print(f"所持金は{gamer.get_money()}円になりました。")

        # Mementoの取り扱いの決定
        if gamer.get_money() > memento.get_money():
            print("※だいぶ増えたので、現在の状態を保存しておこう！")
            memento = gamer.create_memento()
        elif gamer.get_money() < memento.get_money() / 2:
            print("※だいぶ減ったので、以前の状態を復元しよう！")
            gamer.restore_memento(memento)

        # 時間待ち
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            pass
        print()


if __name__ == "__main__":
    main()
