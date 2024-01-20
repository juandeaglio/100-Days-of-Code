"""Unit tests for band generators"""
import pytest
from typing import List

from question_answer import QuestionAnswer
from simple_band_generator import SimpleBandGenerator


@pytest.fixture
def questions_fixture():
    expected = ["What's the name of the city you grew up in?", "What's your pet's name?"]
    return expected
@pytest.fixture()
def answers_fixture():
    answers = ["Tarzana", "Kevin"]
    return answers


def test_list_questions(questions_fixture):
    band_generator = SimpleBandGenerator()
    assert band_generator.list_questions() == questions_fixture


def test_question_answer(questions_fixture, answers_fixture):
    band_generator = SimpleBandGenerator()
    pairs = band_generator.ask_questions()
    expected: List[QuestionAnswer] = [QuestionAnswer(question=questions_fixture[0], answer=answers_fixture[0])]
    assert pairs == expected
