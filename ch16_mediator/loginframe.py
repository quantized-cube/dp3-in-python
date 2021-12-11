import sys
from typing import Any
from colleague import ColleagueButton, ColleagueCheckbox, ColleagueTextField
from mediator import Mediator


ActionEvent = str


class LoginFrame(Mediator):
    # Colleagueたちを生成し、配置後に表示する
    def __init__(self, title: str) -> None:
        self.frame_title = title

        # 背景色を設定する
        self.background = "lightGray"

        # レイアウトマネージャを使って4×2のグリッドを作る
        self.layout: list[list[Any]] = [
            [None] * 2 for _ in range(4)
        ]

        # Colleagueたちを生成する
        self.create_colleagues()

        # 配置する
        self.layout[0][0] = self.check_guest
        self.layout[0][1] = self.check_login
        self.layout[1][0] = "[Label] Username:"
        self.layout[1][1] = self.text_user
        self.layout[2][0] = "[Label] Password:"
        self.layout[2][1] = self.text_pass
        self.layout[3][0] = self.button_ok
        self.layout[3][1] = self.button_cancel

        # 有効/無効の初期指定をする
        self.colleague_changed()

        # 表示する
        self.show()

        while True:
            self.change_state()

    # Colleagueたちを生成する
    def create_colleagues(self) -> None:
        # CheckBox
        g = "CheckboxGroup1"
        self.check_guest = ColleagueCheckbox("Guest", g, True)
        self.check_login = ColleagueCheckbox("Login", g, False)

        # TextField
        self.text_user = ColleagueTextField("", 10)
        self.text_pass = ColleagueTextField("", 10)
        self.text_pass.set_echo_char('*')

        # Button
        self.button_ok = ColleagueButton("OK")
        self.button_cancel = ColleagueButton("Cancel")

        # Mediatorを設定する
        self.check_guest.set_mediator(self)
        self.check_login.set_mediator(self)
        self.text_user.set_mediator(self)
        self.text_pass.set_mediator(self)
        self.button_ok.set_mediator(self)
        self.button_cancel.set_mediator(self)

        print("usage:")
        print("check guest/login")
        print("user (str)")
        print("pass (str)")
        print("button ok/cancel")

    def change_state(self) -> None:
        text = input("input: ")
        if text == "check guest":
            self.check_guest.checkbox_state = True
            self.check_login.checkbox_state = False
            self.colleague_changed()
        elif text == "check login":
            self.check_guest.checkbox_state = False
            self.check_login.checkbox_state = True
            self.colleague_changed()
        elif text.startswith("user "):
            if self.text_user.text_field_enabled:
                self.text_user.text_field_text = text[5:]
                self.colleague_changed()
            else:
                print("disabled!!")
        elif text.startswith("pass "):
            if self.text_pass.text_field_enabled:
                self.text_pass.text_field_text = text[5:]
                self.colleague_changed()
            else:
                print("disabled!!")
        elif text == "button ok":
            if self.button_ok.button_enabled:
                self.action_performed("ok clicked")
            else:
                print("disabled!!")
        elif text == "button cancel":
            if self.button_cancel.button_enabled:
                self.action_performed("cancel clicked")
            else:
                print("disabled!!")
        else:
            print("?")
        self.show()

    # Colleageの状態が変化したときに呼ばれる
    def colleague_changed(self) -> None:
        if self.check_guest.get_state():
            # ゲストログイン
            self.text_user.set_colleague_enabled(False)
            self.text_pass.set_colleague_enabled(False)
            self.button_ok.set_colleague_enabled(True)
        else:
            # ユーザログイン
            self.text_user.set_colleague_enabled(True)
            self._userpass_changed()

    # text_userまたはtext_passの変更があった
    # 各Colleageの有効/無効を判定する
    def _userpass_changed(self) -> None:
        if len(self.text_user.get_text()) > 0:
            self.text_pass.set_colleague_enabled(True)
            if len(self.text_pass.get_text()) > 0:
                self.button_ok.set_colleague_enabled(True)
            else:
                self.button_ok.set_colleague_enabled(False)
        else:
            self.text_pass.set_colleague_enabled(False)
            self.button_ok.set_colleague_enabled(False)

    def action_performed(self, e: ActionEvent) -> None:
        print(e)
        sys.exit()

    def show(self) -> None:
        print("-" * 50)
        print(f"*** {self.frame_title} ***")
        print("\n".join([str([str(i) for i in j]) for j in self.layout]))
        print("-" * 50)
