# abstract_input_stream.py
"""Abstract class for optionally taking in pre-determined input instead of stdin"""
from abc import ABC


class AbstractInputStream(ABC):
    @classmethod
    def input(cls, prompt: str = "") -> str:
        pass
