"""A simple hardcoded band generator."""
from queue import Queue
from typing import List
from band_generator import IBandGenerator
from question_answer import QuestionAnswer


class SimpleBandGenerator(IBandGenerator):
    def __init__(self):
        self._questions: List[str] = ["What's the name of the city you grew up in?",
                                      "What's your pet's name?"]

    def list_questions(self):
        return self._questions

    def ask_questions(self):
        pairs: List[QuestionAnswer] = []
        queue = Queue()

        for question in self._questions:
            queue.put(question)
        question: str = queue.get()
        answers = ["Tarzana", "Kevin"]

        while len(question) > 0:
            print(question)
            answer = answers.pop(0)
            pairs.append(QuestionAnswer(question, answer))
            if not queue.empty():
                question = queue.get()
            else:
                question = ''

        return pairs

