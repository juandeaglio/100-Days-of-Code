from abc import ABC, abstractmethod
from typing import List


class IBandGenerator(ABC):
    @abstractmethod
    def __init__(self):
        self.__questions: List[str] = []

    @abstractmethod
    def list_questions(self):
        pass
