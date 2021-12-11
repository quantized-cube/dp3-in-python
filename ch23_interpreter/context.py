from __future__ import annotations
import re
from ParseException import ParseException


class Context:

    def __init__(self, text: str) -> None:
        self._tokens = re.split(r"\s+", text)
        self._index = 0
        self.next_token()

    def next_token(self) -> str:
        if self._index < len(self._tokens):
            self._last_token = self._tokens[self._index]
            self._index += 1
        else:
            self._last_token = None
        return self._last_token

    def current_token(self) -> str:
        return self._last_token

    def skip_token(self, token: str) -> None:
        current_token = self.current_token()
        if current_token is None:
            raise ParseException(
                f"Error: '{token}' is expected, but no more token is found.")
        elif token != current_token:
            raise ParseException(
                f"Error: '{token}' is expected, but '{current_token}' is found.")
        self.next_token()

    def current_number(self) -> int:
        current_token = self.current_token()
        if current_token is None:
            raise ParseException("Error: No more token.")
        number = 0
        try:
            number = int(current_token)
        except ValueError as e:
            raise ParseException(f"Error: {e}")
        return number
