from math import ceil


floors, apartments_on_floor, window_height, window_width = map(int, input().strip().split())
apartments_count = floors * apartments_on_floor
windows_on_floor_count = window_height * window_width
half_windows_on_floor_count = ceil(windows_on_floor_count / 2.0)
rows = floors * window_height
row_len = apartments_on_floor * window_width
awake = 0

windows: str = ""
for _ in range(rows):
    windows += input().strip()[:row_len]
    if len(windows) // windows_on_floor_count > 0:
        if windows[:windows_on_floor_count].count('X') >= half_windows_on_floor_count:
            awake += 1
        windows = windows[windows_on_floor_count:]
print(awake)
