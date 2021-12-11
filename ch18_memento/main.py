import time
from game import Gamer


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
