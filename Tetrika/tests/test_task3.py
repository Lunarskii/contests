import pytest

from task3.solution import (
    intersect,
    merge_intervals,
    intersect_two_lists,
    appearance,
)


@pytest.mark.parametrize(
    "interval1, interval2, expected",
    [
        ((1, 10), (5, 20), (5, 10)),
    ],
)
def test__intersect__intersecting_intervals(interval1, interval2, expected):
    assert intersect(interval1, interval2) == expected


@pytest.mark.parametrize(
    "interval1, interval2, expected",
    [
        ((1, 10), (1, 5), (1, 5)),
        ((1, 5), (1, 10), (1, 5)),
        ((1, 10), (3, 8), (3, 8)),
    ],
)
def test__intersect__interval_within_another_interval(interval1, interval2, expected):
    assert intersect(interval1, interval2) == expected


def test__intersect__not_intersecting_intervals():
    interval1 = (1, 10)
    interval2 = (11, 20)
    assert intersect(interval1, interval2) is None


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([(1, 10), (5, 20)], [(1, 20)]),
        ([(1, 10), (5, 20), (3, 8), (4, 5), (1, 25), (20, 40)], [(1, 40)]),
    ],
)
def test__merge_intervals__intersecting_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([(1, 10), (5, 20), (25, 40), (30, 35)], [(1, 20), (25, 40)]),
    ],
)
def test__merge_intervals__not_intersecting_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected


@pytest.mark.parametrize(
    "lst1, lst2, expected",
    [
        ([(1, 10), (20, 30), (31, 40)], [(5, 25), (28, 33)], [(5, 10), (20, 25), (28, 30), (31, 33)]),
    ],
)
def test__intersect_two_lists(lst1, lst2, expected):
    assert intersect_two_lists(lst1, lst2) == expected


@pytest.mark.parametrize(
    "intervals, expected",
    [
        (
            {
                "lesson": [1594663200, 1594666800],
                "pupil": [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
                "tutor": [1594663290, 1594663430, 1594663443, 1594666473],
            },
            3117,
        ),
        (
            {
                "lesson": [1594702800, 1594706400],
                "pupil": [
                    1594702789,
                    1594704500,
                    1594702807,
                    1594704542,
                    1594704512,
                    1594704513,
                    1594704564,
                    1594705150,
                    1594704581,
                    1594704582,
                    1594704734,
                    1594705009,
                    1594705095,
                    1594705096,
                    1594705106,
                    1594706480,
                    1594705158,
                    1594705773,
                    1594705849,
                    1594706480,
                    1594706500,
                    1594706875,
                    1594706502,
                    1594706503,
                    1594706524,
                    1594706524,
                    1594706579,
                    1594706641,
                ],
                "tutor": [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463],
            },
            3577,
        ),
        (
            {
                "lesson": [1594692000, 1594695600],
                "pupil": [1594692033, 1594696347],
                "tutor": [1594692017, 1594692066, 1594692068, 1594696341],
            },
            3565,
        ),
    ],
)
def test__appearance(intervals, expected):
    assert appearance(intervals) == expected
