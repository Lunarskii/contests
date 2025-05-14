def has_arithmetic_progression(sequence: list[int]):
    sequence_len = len(sequence)
    for i in range(sequence_len):
        for j in range(i + 1, sequence_len):
            for k in range(j + 1, sequence_len):
                if sequence[j] - sequence[i] == sequence[k] - sequence[j]:
                    return True
    return False


def count_sub_arrays_with_ap(numbers: list[int]):
    numbers_len: int = len(numbers)
    left: int = 0
    safe_count: int = 0
    sub_array: list[int] = []

    for right in range(numbers_len):
        sub_array.append(numbers[right])
        while has_arithmetic_progression(sub_array):
            sub_array.pop(0)
            left += 1
        safe_count += (right - left + 1)

    total_sub_arrays: int = numbers_len * (numbers_len + 1) // 2
    return total_sub_arrays - safe_count


input()
numbers: list[int] = list(map(int, input().split()))
print(count_sub_arrays_with_ap(numbers))
