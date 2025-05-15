from abc import (
    ABC,
    abstractmethod,
)

from metrics import Metric


class Report(ABC):
    def generate(self, metrics: list[Metric]):
        data: dict = {}
        for m in metrics:
            data.update(m.result())
        return self._format(data)

    @abstractmethod
    def _format(self, data): ...


class TableReport(Report):
    def __init__(
        self,
        columns: tuple | list[str],
        aliases: dict[str, str] | None = None,
    ):
        if aliases is None:
            aliases = {}

        self.__columns = columns
        self.__aliases = aliases

    def _format(self, data: list | dict[str, list | dict]) -> str:
        header: str = "".join(f"{self.__aliases.get(column, column):20}" for column in self.__columns)
        rows: list[str] = []

        match data:
            case list():
                index: int = 0
                while (modifier := index + len(self.__columns) - 1) < len(data):
                    rows.append("".join(f"{value:20}" for value in data[index:modifier + 1]))
                    index = modifier + 1
            case dict():
                for key, value in data.items():
                    match value:
                        case list():
                            rows.append("".join(f"{value_:20}" for value_ in [key] + value))
                        case dict():
                            rows.append(
                                "".join(
                                    f"{value_:20}"
                                    for value_ in [key]
                                    + [f"{data[key].get(column, 0)!r}" for column in self.__columns[1:]]
                                )
                            )

        return "\n".join([header] + rows)
