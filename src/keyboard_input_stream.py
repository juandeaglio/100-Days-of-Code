# keyboard_input_stream.py
"""Class for using the default stdin as input"""
from .abstract_input_stream import AbstractInputStream


class KeyboardInputStream(AbstractInputStream):
    @classmethod
    def input(cls, prompt=None) -> str:
        return input()
