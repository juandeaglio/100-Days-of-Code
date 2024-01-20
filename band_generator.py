"""Module for band generator declaration"""
from abc import ABC, abstractmethod


# Creates a band from questions
class IBandGenerator(ABC):
    @abstractmethod
    def __init__(self):
        pass


    @abstractmethod
    def list_questions(self):
        pass
