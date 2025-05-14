_, a_cost, b_cost = map(int, input().split())
s: str = input()
left_bracket_cnt: int = 0
right_bracket_cnt: int = 0

for char in s:
    match char:
        case "(":
            left_bracket_cnt += 1
        case ")":
            if left_bracket_cnt:
                left_bracket_cnt -= 1
            else:
                right_bracket_cnt += 1

number_of_swaps: int = min(left_bracket_cnt, right_bracket_cnt)
left_bracket_cnt -= number_of_swaps
right_bracket_cnt -= number_of_swaps
number_of_changes: int = max(left_bracket_cnt, right_bracket_cnt) // 2

print(number_of_swaps * a_cost + number_of_changes * b_cost)
