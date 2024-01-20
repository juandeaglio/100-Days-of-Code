"""Unit tests for band generators"""
import pytest
from typing import List

from simple_band_generator import SimpleBandGenerator


class QuestionAnswer:
    """A class for pairing an answer to a question."""
    pass


@pytest.fixture
def questions_fixture():
    expected = ["What's the name of the city you grew up in?", "What's your pet's name?"]
    return expected


def test_list_questions(questions_fixture):
    band_generator = SimpleBandGenerator()
    assert band_generator.list_questions() == questions_fixture


def test_question_answer(questions_fixture):
    band_generator = SimpleBandGenerator()
    answers = band_generator.ask_questions()
    expected: List[QuestionAnswer] = []
