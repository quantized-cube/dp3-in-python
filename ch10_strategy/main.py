import sys

from Player import Player
from Strategy import WinningStrategy, ProbStrategy


def main(*args: str) -> None:
    if len(args) != 2:
        print("Usage: python main.py randomseed1 randomseed2")
        print("Example: python main.py 314 15")
        sys.exit()
    seed1 = int(args[0])
    seed2 = int(args[1])
    player1 = Player("Taro",  WinningStrategy(seed1))
    player2 = Player("Hana",  ProbStrategy(seed2))
    for _ in range(10000):
        next_hand1 = player1.next_hand()
        next_hand2 = player2.next_hand()
        if next_hand1.isStrongerThan(next_hand2):
            print(f"Winner: {player1}")
            player1.win()
            player2.lose()
        elif next_hand2.isStrongerThan(next_hand1):
            print(f"Winner: {player2}")
            player1.lose()
            player2.win()
        else:
            print("Even...")
            player1.even()
            player2.even()
    print("Total result:")
    print(player1)
    print(player2)


if __name__ == "__main__":
    args = sys.argv
    main(*args[1:])
