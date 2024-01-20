"""A simple hardcoded band generator."""
from typing import List
from band_generator import IBandGenerator
from question_answer import QuestionAnswer


class SimpleBandGenerator(IBandGenerator):
    def __init__(self):
        self.__questions: List[str] = ["What's the name of the city you grew up in?",
                            "What's your pet's name?"]

    def list_questions(self):
        return self.__questions


    def ask_questions(self):
        return [QuestionAnswer()]
