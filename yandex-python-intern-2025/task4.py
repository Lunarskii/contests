from collections import deque


def max_square_size(
    rows: int,
    cols: int,
    max_distance: int,
    grid: list[list[str]],
):
    queue: deque[tuple[int, int]] = deque()
    occupied: list[list[int]] = [[-1] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'x':
                queue.append((i, j))
                occupied[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx: int = x + dx
            ny: int = y + dy
            if 0 <= nx < rows and 0 <= ny < cols and occupied[nx][ny] == -1:
                occupied[nx][ny] = occupied[x][y] + 1
                if occupied[nx][ny] < max_distance - 1:
                    queue.append((nx, ny))

    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if occupied[i][j] == -1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
    return max_side


if __name__ == "__main__":
    rows, cols, max_distance = map(int, input().strip().split())
    grid: list[list[str]] = [list(input().strip()) for _ in range(rows)]
    print(max_square_size(rows, cols, max_distance, grid))
