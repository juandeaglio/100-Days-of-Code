"""Abstract class for optionally taking in pre-determined input instead of stdin"""
from abc import ABC, abstractmethod


class AbstractInputStream(ABC):
    @abstractmethod
    def __init__(self, answers: str = None):
        return

    @abstractmethod
    def get_input(self):
        pass
