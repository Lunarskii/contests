input()
heights: list[int] = list(map(int, input().split()))
sum_diff: int = 0

while len(heights) > 2:
    index: int = 0
    current_diff: int = 0

    while index < len(heights) - 1 and current_diff < (new_diff := abs(heights[index] - heights[index + 1])):
        current_diff = new_diff
        index += 1
    sum_diff += current_diff
    del heights[index - 1:index + 1]
if len(heights) == 2:
    sum_diff += abs(heights[0] - heights[1])
print(sum_diff)
