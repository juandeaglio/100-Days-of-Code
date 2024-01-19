import pytest

from SimpleBandGenerator import SimpleBandGenerator


@pytest.fixture
def questions_fixture():
    expected = ["What's the name of the city you grew up in?", "What's your pet's name?"]
    return expected


def test_show_questions(questions_fixture):
    band_generator = SimpleBandGenerator()
    assert band_generator.list_questions() == questions_fixture
