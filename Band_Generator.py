import unittest
from abc import ABC, abstractmethod
from typing import List


class BandGenerator(ABC):
    @abstractmethod
    def __init__(self):
        self.__questions: List[str] = []

    @abstractmethod
    def list_questions(self):
        pass


class SimpleBandGenerator(BandGenerator):
    def __init__(self):
        self.__questions = ["What's the name of the city you grew up in?", "What's your pet's name?"]

    def list_questions(self):
        return self.__questions


class BandGeneratorTestCase(unittest.TestCase):
    def test_show_questions(self):
        expected = ["What's the name of the city you grew up in?", "What's your pet's name?"]
        band_generator = SimpleBandGenerator()
        self.assertEqual(band_generator.list_questions(), expected)

if __name__ == '__main__':
    unittest.main()
