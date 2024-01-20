"""A simple hardcoded band generator."""
from queue import Queue
from typing import List
from band_generator import IBandGenerator
from question_answer import QuestionAnswer
from abstract_input_stream import AbstractInputStream


class SimpleBandGenerator(IBandGenerator):
    def __init__(self):
        self._questions: List[str] = ["What's the name of the city you grew up in?",
                                      "What's your pet's name?"]
        self.queue: Queue = self.queue_questions()

    def queue_questions(self):
        queue = Queue()
        for question in self._questions:
            queue.put(question)

        return queue

    def list_questions(self):
        return self._questions

    def ask_questions(self, input_stream: AbstractInputStream):
        pairs: List[QuestionAnswer] = []

        question: str = self.queue.get()
        answers = ["Tarzana", "Kevin"]

        while len(question) > 0:
            self.query_user(question)
            answer = input_stream.get_input()
            pairs.append(QuestionAnswer(question, answer))
            if not self.queue.empty():
                question = self.queue.get()
            else:
                question = ''

        return pairs

    def query_user(self, question):
        print(question)
