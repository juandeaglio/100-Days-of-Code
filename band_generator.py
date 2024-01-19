"""Module for band generator declaration"""
from abc import ABC, abstractmethod
from typing import List


# Creates a band from questions
class IBandGenerator(ABC):
    @abstractmethod
    def __init__(self):
        self._questions: List[str] = []



    @abstractmethod
    def list_questions(self):
        pass
