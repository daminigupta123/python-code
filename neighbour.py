n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]
x, y = map(int, input().split())
x -= 1  # convert to 0-based index
y -= 1
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]
for dx, dy in directions:
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m:
        if grid[nx][ny] != 'x':
            print("no")
            break
else:
    print("yes")
