# simple_band_generator.py
"""A simple hardcoded band generator."""
from queue import Queue
from typing import List, Callable

from .band_generator import IBandGenerator
from .question_answer import QuestionAnswer
from .keyboard_input_stream import KeyboardInputStream


class SimpleBandGenerator(IBandGenerator):
    def __init__(self):
        self.pairs: List[QuestionAnswer] = []
        self.__questions: List[str] = ["What's the name of the city you grew up in?",
                                       "What's your pet's name?"]
        self.queue: Queue = self.queue_questions()

    def queue_questions(self):
        queue = Queue()
        for question in self.__questions:
            queue.put(question)

        return queue

    def list_questions(self):
        return self.__questions

    def ask_questions(self, input_stream: Callable[..., str] = KeyboardInputStream().input):
        pairs: List[QuestionAnswer] = []

        question: str = self.queue.get()

        while len(question) > 0:
            self.query_user(question)
            answer = input_stream()
            pairs.append(QuestionAnswer(question, answer))
            if not self.queue.empty():
                question = self.queue.get()
            else:
                question = ''

        self.pairs = pairs
        return pairs

    def query_user(self, question):
        print(question)

    def form_band_name(self):
        return " ".join(str(pair) for pair in self.pairs)

    def suggest_band_name(self) -> str:
        return "Your band name could be " + self.form_band_name()
