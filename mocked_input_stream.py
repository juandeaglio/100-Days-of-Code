# mocked_input_stream.py

"""Class for using a mocked set of inputs (without the need of using a keyboard)"""
from typing import List

from abstract_input_stream import AbstractInputStream


class MockedInputStream(AbstractInputStream):
    __answers: List[str] = []

    @classmethod
    def input(cls, prompt=None) -> str:
        if prompt is None:
            prompt = []

        if len(prompt) == 0:
            return cls.__answers.pop(0)

        cls.__answers = prompt.copy()
        return ''
