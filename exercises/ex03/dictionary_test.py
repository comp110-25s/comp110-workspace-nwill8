"""Testing my practice with dictionaries!"""

__author__: str = "730580318"

import pytest
from exercises.ex03.dictionary import invert, favorite_color, count, bin_len


def test_invert_use_case():
    assert invert({"1": "9", "2": "8"}) == {"9": "1", "8": "2"}


def test_invert_use_case_two():
    assert invert({"dog": "cat"}) == {"cat": "dog"}


def test_invert_edge_case():
    with pytest.raises(KeyError):
        assert invert({"apple": "orange", "banana": "orange"})


def test_count_use_case():
    assert count(["apple", "banana", "apple", "cherry"]) == {
        "apple": 2,
        "banana": 1,
        "cherry": 1,
    }


def test_count_use_case_two():
    assert count(["one", "two", "three"]) == {"one": 1, "two": 1, "three": 1}


def test_count_edge_case():
    assert count([]) == {}


def test_favorit_color_use_case():
    assert favorite_color({"Alice": "blue", "Bob": "blue", "Kevin": "red"}) == "blue"


def test_favorite_color_use_case_two():
    assert (
        favorite_color({"Alice": "blue", "Bob": "red", "Kevin": "red", "David": "blue"})
        == "blue"
    )


def test_favorite_color_edge_case():
    assert favorite_color({"Alice": "blue"}) == "blue"


def test_bin_len_use_case():
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_len_use_case_two():
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}


def test_bin_len_edge_case():
    assert bin_len([]) == {}
