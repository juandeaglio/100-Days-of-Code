"""Unit tests for band generators"""
from queue import Queue, Empty
from typing import List

import pytest

from abstract_input_stream import AbstractInputStream
from question_answer import QuestionAnswer
from simple_band_generator import SimpleBandGenerator


class MockedInputStream(AbstractInputStream):
    def __init__(self, questions):
        self.stream = Queue()
        for question in questions:
            self.stream.put(question)

    def get_input(self):
        try:
            return self.stream.get(block=False)
        except Empty as exc:
            raise exc


@pytest.fixture
def questions_fixture():
    expected = ["What's the name of the city you grew up in?", "What's your pet's name?"]
    return expected


@pytest.fixture()
def answers_fixture():
    answers = ["Tarzana", "Kevin"]
    return answers


@pytest.fixture()
def simulated_answers(answers_fixture):
    answers = MockedInputStream(answers_fixture)
    return answers


def test_list_questions(questions_fixture):
    band_generator = SimpleBandGenerator()
    assert band_generator.list_questions() == questions_fixture


def test_question_answer(questions_fixture, answers_fixture, simulated_answers):
    band_generator = SimpleBandGenerator()
    pairs = band_generator.ask_questions(simulated_answers)
    expected: List[QuestionAnswer] = [QuestionAnswer(question=questions_fixture[0],
                                                     answer=answers_fixture[0]),
                                      QuestionAnswer(question=questions_fixture[1],
                                                     answer=answers_fixture[1])]
    assert pairs == expected
