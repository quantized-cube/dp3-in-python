from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Any
from mediator import Mediator


class Colleague(metaclass=ABCMeta):
    @abstractmethod
    def set_mediator(self, mediator: Mediator) -> None:
        # Mediatorを設定する
        pass

    @abstractmethod
    def set_colleague_enabled(self, enabled: bool) -> None:
        # Mediatorから有効/無効が指示される
        pass


class ColleagueButton(Colleague):
    def __init__(self, caption: str) -> None:
        self.button_caption = caption
        self.button_enabled = True

    # Mediatorを設定する
    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator

    # Mediatorから有効/無効が指示される
    def set_colleague_enabled(self, enabled: bool) -> None:
        self.button_enabled = enabled

    def __str__(self) -> str:
        state = "enabled" if self.button_enabled else "disabled"
        return f"<Button ({state})> {self.button_caption}"


CheckboxGroup = str
ItemEvent = Any
TextEvent = Any


class ColleagueCheckbox(Colleague):
    def __init__(self, caption: str, group: CheckboxGroup, state: bool) -> None:
        self.checkbox_caption = caption
        self.checkbox_group = group
        self.checkbox_state = state

    # Mediatorを設定する
    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator

    # Mediatorから有効/無効が指示される
    def set_colleague_enabled(self, enabled: bool) -> None:
        self.checkbox_enabled = enabled

    # 状態が変化したらMediatorに通知する
    def item_state_changed(self, e: ItemEvent) -> None:
        self.mediator.colleague_changed()

    def get_state(self) -> bool:
        return self.checkbox_state

    def __str__(self) -> str:
        state = "selected" if self.checkbox_state else "unselected"
        return f"<Checkbox> {self.checkbox_caption}: {state}"


class ColleagueTextField(Colleague):
    def __init__(self, text: str, columns: int) -> None:
        self.text_field_text = text
        self.text_field_columns = columns
        self.echo_char: str | None = None
        self.text_field_enabled = False

    # Mediatorを設定する
    def set_mediator(self, mediator: Mediator) -> None:
        self.mediator = mediator

    # Mediatorから有効/無効が指示される
    def set_colleague_enabled(self, enabled: bool) -> None:
        self.text_field_enabled = enabled
        # 有効/無効に合わせて背景色を変更する
        self.text_field_background = "white" if enabled else "lightGray"

    # 文字列が変化したらMediatorに通知する
    def text_value_changed(self, e: TextEvent) -> None:
        self.mediator.colleague_changed

    def set_echo_char(self, char: str) -> None:
        assert len(char) == 1
        self.echo_char = char

    def get_text(self) -> str:
        return self.text_field_text

    def __str__(self) -> str:
        state = "enabled" if self.text_field_enabled else "disabled"
        if self.echo_char is None:
            return f"<TextField ({state})> {self.text_field_text}"
        else:
            return f"<TextField ({state})> {self.echo_char * len(self.text_field_text)}"
