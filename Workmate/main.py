import argparse

from handlers import (
    LogHandler,
    HTTPDjangoRequestHandler,
)
from metrics import (
    Metric,
    EndpointLogLevelCounter,
)
from report import (
    Report,
    TableReport,
)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="+")
    parser.add_argument("--report")

    args: argparse.Namespace = parser.parse_args()
    handler: LogHandler = HTTPDjangoRequestHandler()
    metric: Metric = EndpointLogLevelCounter(
        modules={"django.request"},
        log_levels={"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"},
    )

    for file_name in args.files:
        with open(file_name) as fd:
            while line := fd.readline():
                if handled_str := handler.handle(line):
                    metric.process(handled_str)

    report: Report = TableReport(
        columns=("endpoint", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"), aliases={"endpoint": "HANDLER"}
    )
    print(report.generate([metric]))
