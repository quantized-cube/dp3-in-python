from context import Context
from node import ProgramNode


def main() -> None:
    try:
        with open("program.txt", "r") as f:
            lines = f.read().splitlines()
        for text in lines:
            print(f'text = "{text}"')
            node = ProgramNode()
            node.parse(Context(text))
            print(f"node = {node}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
