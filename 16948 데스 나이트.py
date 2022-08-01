import sys
from collections import deque

n = int(input())

mapGraph = [[0 for i in range(n)] for i in range(n)]
visited = [[0 for i in range(n)] for i in range(n)]
dir = [[-2, -1], [-2, +1], [0, -2], [0, +2], [+2, -1], [+2, +1]]

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
queue = deque()
visited[r1][c1] = 1
queue.append((r1, c1))
mapGraph[r1][c1] = 0

while queue:
    x, y = queue.popleft()

    if x == r2 and y == c2:
        print(mapGraph[x][y])
        break

    for i in range(6):
        dx = x + dir[i][0]
        dy = y + dir[i][1]

        if dx < 0 or dx >= n or dy < 0 or dy >= n:
            continue

        if visited[dx][dy] == 0:
            queue.append((dx, dy))
            visited[dx][dy] = 1
            mapGraph[dx][dy] = mapGraph[x][y] + 1
else:
    print(-1)
