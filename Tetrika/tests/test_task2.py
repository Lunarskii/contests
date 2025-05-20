from task2.solution import (
    get_category_members,
    get_count_of_beasts_alphabetically,
)


def test_wrong_category_to_parse():
    assert get_category_members(title="_unknown_category_", cm_prop="title", cm_type="page") == []


def test_right_category_to_parse():
    category_members: list[int] = get_category_members(title="Животные_по_алфавиту", cm_prop="title", cm_type="page")
    assert len(category_members) != 0


def test_beasts_are_sorted():
    beasts: dict[str, int] = get_count_of_beasts_alphabetically()

    def alphabet_index(char: str):
        if ord("А") <= ord(char) <= ord("Е"):
            return 0
        elif char == "Ё" or ord("Ж") <= ord(char) <= ord("Я"):
            return 1
        return 2

    assert len(beasts) != 0
    assert dict(sorted(beasts.items(), key=lambda x: (alphabet_index(x[0]), x[0]))) == beasts
