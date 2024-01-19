import pytest
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


@pytest.fixture
def questions_fixture():
    expected = ["What's the name of the city you grew up in?", "What's your pet's name?"]
    return expected


def test_show_questions(questions_fixture):
    band_generator = SimpleBandGenerator()
    assert band_generator.list_questions() == questions_fixture
