import sys
from collections import deque

dir=[[0,1],[1,0],[0,-1],[-1,0]]

n=int(input())
graph=[list(map(int,sys.stdin.readline().split()))for i in range(n)]
visited=[[0 for i in range(n)]for i in range(n)]
dir_cost=[[0 for i in range(n)]for i in range(n)]

dir_visited=[[0 for i in range(n)]for i in range(n)]

queue=deque()
tempQueue=deque()

current_size=2
level=0
total_result=0

for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            queue.append((i,j,0))
            graph[i][j]=0


def shark_BFS():

    while queue:
        x, y,z_cost = queue.popleft()
        visited[x][y] = 1

        if graph[x][y] != 0 and graph[x][y]<current_size:
            tempQueue.append((x,y,dir_cost[x][y]))


        for i in range(4):
            dx = x + dir[i][0]
            dy = y + dir[i][1]

            if dx < 0 or dx >= n or dy < 0 or dy >= n:
                continue

            if graph[dx][dy] <= current_size and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                dir_cost[dx][dy] = dir_cost[x][y] + 1
                queue.append((dx, dy,dir_cost[dx][dy]))


shark_BFS()

while True:
    tempQueue = list(tempQueue)
    tempQueue.sort(key=lambda x:x[2])
    tempQueue = deque(tempQueue)

    tempx, tempy,tempz = tempQueue[0]
    dir_visited[tempx][tempy]=1

    tempQueue = deque()
    total_result += dir_cost[tempx][tempy]
    level += 1


    queue=deque()
    queue.append((tempx,tempy,tempz))
    visited=[[0 for i in range(n)]for i in range(n)]
    dir_cost = [[0 for i in range(n)] for i in range(n)]

    if current_size == level:
        current_size += 1
        level=0

    shark_BFS()

    if not tempQueue:
        print(total_result)
        break







