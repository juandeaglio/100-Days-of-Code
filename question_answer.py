# question_answer.py
"""A class for pairing an answer to a question."""


class QuestionAnswer:
    def __init__(self, question: str = None, answer: str = None):
        self.__answer = None
        self.__question = None
        self.set_question(question)
        self.set_answer(answer)

    def set_question(self, question):
        self.__question = question

    def set_answer(self, answer):
        self.__answer = answer

    def get_question(self):
        return self.__question

    def get_answer(self):
        return self.__answer

    def __eq__(self, other):
        return self.__question == other.get_question() and self.__answer == other.get_answer()

    def __str__(self):
        return self.__answer
