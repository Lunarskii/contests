from typing import Literal
from collections import Counter
import csv

from requests import (
    Response,
    Session,
)


API_URL: str = "https://ru.wikipedia.org/w/api.php"


def get_category_members(
    title: str,
    cm_prop: str,
    cm_type: str,
    cm_limit: int = 500,
    format_: Literal["json", "jsonfm", "none", "php", "phpfm", "rawfm", "xml", "xmlfm"] = "json",
) -> list[str]:
    members: list[str] = []
    params: dict[str, str] = {
        "action": "query",
        "list": "categorymembers",
        "cmtitle": f"Категория:{title}",
        "cmprop": cm_prop,
        "cmtype": cm_type,
        "cmlimit": str(cm_limit),
        "format": format_,
    }
    session: Session = Session()

    while True:
        request: Response = session.get(API_URL, params=params)
        data = request.json()
        members.extend(item["title"] for item in data["query"]["categorymembers"])

        if "continue" not in data:
            break

        params.update(data["continue"])

    return members


def get_count_of_beasts_alphabetically() -> dict[str, int]:
    beasts: list[str] = get_category_members(
        title="Животные_по_алфавиту",
        cm_prop="title",
        cm_type="page",
    )
    counter: Counter[str, int] = Counter[str, int]()

    for title in beasts:
        counter[title[0]] += 1

    def alphabet_index(char: str):
        if ord("А") <= ord(char) <= ord("Е"):
            return 0
        elif char == "Ё" or ord("Ж") <= ord(char) <= ord("Я"):
            return 1
        return 2

    return dict(sorted(counter.items(), key=lambda x: (alphabet_index(x[0]), x[0])))


if __name__ == "__main__":
    beasts: dict[str, int] = get_count_of_beasts_alphabetically()

    with open("beasts.csv", "w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(beasts.items())
