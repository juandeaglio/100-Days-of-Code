# test_band_generator.py

"""Unit tests for band generators"""
from typing import List

import pytest

from mocked_input_stream import MockedInputStream
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


@pytest.fixture()
def simulated_answers_fixture(answers_fixture):
    MockedInputStream.input(answers_fixture)
    input_answers = MockedInputStream.input
    return input_answers


def test_list_questions(questions_fixture):
    band_generator = SimpleBandGenerator()
    assert band_generator.list_questions() == questions_fixture


def test_question_answer(questions_fixture, answers_fixture, simulated_answers_fixture):
    band_generator = SimpleBandGenerator()
    pairs = band_generator.ask_questions(simulated_answers_fixture)
    expected: List[QuestionAnswer] = [QuestionAnswer(question=questions_fixture[0],
                                                     answer=answers_fixture[0]),
                                      QuestionAnswer(question=questions_fixture[1],
                                                     answer=answers_fixture[1])]

    assert pairs == expected


def test_create_band_name(questions_fixture, answers_fixture, simulated_answers_fixture):
    band_generator = SimpleBandGenerator()
    pairs: List[QuestionAnswer] = band_generator.ask_questions(simulated_answers_fixture)
    answers: List[str] = [pairs[0].get_answer(), pairs[1].get_answer()]
    name_suggestion = "Your band name could be", " ".join(answers)
    assert band_generator.suggest_band_name() == name_suggestion


# def test_manual_answers(questions_fixture, answers_fixture):
#     # the correct answers are as seen in answers_fixture, type them in that exact order
#     band_generator = SimpleBandGenerator()
#     pairs = band_generator.ask_questions(KeyboardInputStream().input)
#     expected: List[QuestionAnswer] = [QuestionAnswer(question=questions_fixture[0],
#                                                      answer=answers_fixture[0]),
#                                       QuestionAnswer(question=questions_fixture[1],
#                                                      answer=answers_fixture[1])]
#
#     assert pairs == expected
