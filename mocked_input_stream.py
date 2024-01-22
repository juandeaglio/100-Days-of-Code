"""Class for using a mocked set of inputs (without the need of using a keyboard)"""
from typing import List

from abstract_input_stream import AbstractInputStream


class MockedInputStream(AbstractInputStream):
    answers: List[str] = []

    @classmethod
    def input(cls, prompt=None) -> str:
        if prompt is None:
            prompt = []

        if len(prompt) == 0:
            return cls.answers.pop(0)

        cls.answers = prompt.copy()
        return ''
