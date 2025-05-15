from abc import (
    ABC,
    abstractmethod,
)
from typing import LiteralString
import re


"""
надо создать какой-то менеджер обработчиков, в который можно класть несколько обработчиков
чтобы менеджер ими управлял сам
"""


class LogHandler(ABC):
    def handle(self, line: str) -> dict[str, str] | None:
        if parsed := self._parse(line):
            return parsed

    @abstractmethod
    def _parse(self, line: str) -> dict[str, str] | None: ...


class HTTPDjangoRequestHandler(LogHandler):
    log_level_re: LiteralString = r"\b(DEBUG|INFO|WARNING|ERROR|CRITICAL)\b"
    request_re: LiteralString = r"django\.request: (?:(?:[A-Za-z0-9_]+)|(?:[A-Za-z0-9_]+(?: [A-Za-z0-9_]+)*:))"
    endpoint_re: LiteralString = r"(\/[A-Za-z0-9_]+\/(?:[A-Za-z0-9_]+\/)*)"
    pattern: re.Pattern = re.compile(f"{log_level_re} {request_re} {endpoint_re}")

    def _parse(self, line: str) -> dict[str, str]:
        if match := self.pattern.search(line):
            return {"type": "django.request", "log_level": match.group(1), "endpoint": match.group(2)}
