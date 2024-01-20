"""A class for pairing an answer to a question."""


class QuestionAnswer:
    def __init__(self, question: str = None, answer: str = None):
        self._answer = None
        self._question = None
        self.set_question(question)
        self.set_answer(answer)

    def set_question(self, question):
        self._question = question

    def set_answer(self, answer):
        self._answer = answer

    def get_question(self):
        return self._question

    def get_answer(self):
        return self._answer

    def __eq__(self, other):
        return self._question == other.get_question() and self._answer == other.get_answer()
