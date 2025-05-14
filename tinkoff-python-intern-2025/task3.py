def max_distinct_after_div2(numbers: list[int]) -> int:
    used_numbers: set[int] = set()
    numbers.sort(reverse=True)
    for num in numbers:
        while num > 0 and num in used_numbers:
            num //= 2
        used_numbers.add(num)
    return len(used_numbers)


input()
numbers: list[int] = list(map(int, input().split()))
print(max_distinct_after_div2(numbers))
