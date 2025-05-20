from typing import Iterable


def intersect(interval1: tuple[int, int], interval2: tuple[int, int]) -> tuple[int, int] | None:
    start: int = max(interval1[0], interval2[0])
    end: int = min(interval1[1], interval2[1])
    if start < end:
        return start, end


def group_by_n_elements(iterable: Iterable, n: int) -> Iterable:
    for i in range(0, len(iterable), n):
        yield iterable[i:i+n]


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals["lesson"]
    visit_time: int = 0
    common_occurrences: list[tuple[int, int]] = []

    for pupil_visit_start, pupil_visit_end in group_by_n_elements(intervals["pupil"], 2):
        for tutor_visit_start, tutor_visit_end in group_by_n_elements(intervals["tutor"], 2):
            if common_occurrence := intersect((pupil_visit_start, pupil_visit_end), (tutor_visit_start, tutor_visit_end)):
                changed: bool = False

                for interval in common_occurrences[:]:
                    if intersect(interval, common_occurrence):
                        common_occurrences.remove(interval)
                        common_occurrences.append((min(interval[0], common_occurrence[0]), max(interval[1], common_occurrence[1])))
                        changed = True

                if not changed:
                    common_occurrences.append((common_occurrence[0], common_occurrence[1]))

    for start, end in common_occurrences:
        visit_time += -max(start, lesson_start) + min(end, lesson_end)

    return visit_time
