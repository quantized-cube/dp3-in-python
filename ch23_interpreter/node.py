from __future__ import annotations
from abc import ABCMeta, abstractmethod
from context import Context
from ParseException import ParseException


class Node(metaclass=ABCMeta):
    @abstractmethod
    def parse(self, context: Context) -> None:
        pass


# <program> ::= program <command list>
class ProgramNode(Node):

    def parse(self, context: Context) -> None:
        context.skip_token("program")
        self._command__list_node = CommandListNode()
        self._command__list_node.parse(context)

    def __str__(self) -> str:
        return f"[program {self._command__list_node}]"


# <command list> ::= <command>* end
class CommandListNode(Node):
    def __init__(self) -> None:
        self._list_: list[Node] = []

    def parse(self, context: Context) -> None:
        while True:
            if context.current_token() is None:
                raise ParseException("Error: Missing 'end'")
            elif context.current_token() == "end":
                context.skip_token("end")
                break
            else:
                command_node = CommandNode()
                command_node.parse(context)
                self._list_.append(command_node)

    def __str__(self) -> str:
        return "[" + ", ".join(map(str, self._list_)) + "]"


# <command> ::= <repeat command> | <primitive command>
class CommandNode(Node):

    def parse(self, context: Context) -> None:
        self._node: Node
        if context.current_token() == "repeat":
            self._node = RepeatCommandNode()
            self._node.parse(context)
        else:
            self._node = PrimitiveCommandNode()
            self._node.parse(context)

    def __str__(self) -> str:
        return str(self._node)


# <repeat command> ::= repeat <number> <command list>
class RepeatCommandNode(Node):

    def parse(self, context: Context) -> None:
        context.skip_token("repeat")
        self._number = context.current_number()
        context.next_token()
        self._commandListNode = CommandListNode()
        self._commandListNode.parse(context)

    def __str__(self) -> str:
        return f"[repeat {self._number} {self._commandListNode}]"


# <primitive command> ::= go | right | left
class PrimitiveCommandNode(Node):

    def parse(self, context: Context) -> None:
        self._name = context.current_token()
        if self._name is None:
            raise ParseException("Error: Missing <primitive command>")
        elif self._name not in ["go", "right", "left"]:
            raise ParseException(
                "Error: Unknown <primitive command>: '{self._name}'")
        context.skip_token(self._name)

    def __str__(self) -> str:
        return self._name
