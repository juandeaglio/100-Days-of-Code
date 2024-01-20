from abc import ABC, abstractmethod
from typing import List


class AbstractInputStream(ABC):
    @abstractmethod
    def __init__(self, questions: List[str]):
        return

    @abstractmethod
    def get_input(self):
        pass
