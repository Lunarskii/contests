def intersect(interval1: tuple[int, int], interval2: tuple[int, int]) -> tuple[int, int] | None:
    start: int = max(interval1[0], interval2[0])
    end: int = min(interval1[1], interval2[1])
    if start < end:
        return start, end


def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged: list[tuple[int, int]] = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged


def intersect_two_lists(
    lst1: list[tuple[int, int]],
    lst2: list[tuple[int, int]],
) -> list[tuple[int, int]]:
    i: int = 0
    j: int = 0
    result: list[tuple[int, int]] = []

    while i < len(lst1) and j < len(lst2):
        if interval := intersect(lst1[i], lst2[j]):
            result.append(interval)

        if lst1[i][1] < lst2[j][1]:
            i += 1
        else:
            j += 1
    return result


def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals["lesson"]

    def clip_and_pair(lst: list[int]) -> list[tuple[int, int]]:
        pairs = [(max(lesson_start, lst[i]), min(lesson_end, lst[i + 1])) for i in range(0, len(lst), 2)]
        return [interval for interval in pairs if interval[0] < interval[1]]

    pupil: list[tuple[int, int]] = clip_and_pair(intervals["pupil"])
    tutor: list[tuple[int, int]] = clip_and_pair(intervals["tutor"])
    pupil_merged: list[tuple[int, int]] = merge_intervals(pupil)
    tutor_merged: list[tuple[int, int]] = merge_intervals(tutor)
    common_occurrences: list[tuple[int, int]] = intersect_two_lists(pupil_merged, tutor_merged)

    return sum(end - start for start, end in common_occurrences)
