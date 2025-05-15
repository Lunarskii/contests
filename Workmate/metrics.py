from abc import (
    ABC,
    abstractmethod,
)
from collections import defaultdict


class Metric(ABC):
    @abstractmethod
    def process(self, event: dict[str, str]) -> None: ...

    @abstractmethod
    def result(self) -> dict[object, object]: ...


class EndpointLogLevelCounter(Metric):
    def __init__(
        self,
        modules: tuple | list[str] | set[str],
        log_levels: tuple | list[str] | set[str],
    ):
        self.__modules = modules
        self.__log_msg_counter: dict[str, dict[str, int]] = defaultdict(
            lambda: {log_level: 0 for log_level in log_levels}
        )
        self.__total_log_msg_counter: dict[str, int] = defaultdict(int)

    def process(self, event: dict[str, str]) -> None:
        if event.get("type") not in self.__modules:
            return None

        log_level: str = event.get("log_level")
        endpoint: str = event.get("endpoint")

        if log_level and endpoint:
            self.__log_msg_counter[endpoint][log_level] += 1
            self.__total_log_msg_counter[log_level] += 1

    def result(self) -> dict[str, dict[str, int]]:
        final_counter: dict[str, dict[str, int]] = dict(self.__log_msg_counter)
        final_counter["..."] = dict(self.__total_log_msg_counter)
        return final_counter