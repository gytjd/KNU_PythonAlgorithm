import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
graph=[list(map(int,sys.stdin.readline().split()))for i in range(m)]
dir=[[0,1],[1,0],[0,-1],[-1,0]]

queue=deque()
tempQueue=deque()

for i in range(m):
    for j in range(n):
        if graph[i][j]==1:
            queue.append((i,j))


def is_eqaul():
    for i in range(m):
        for j in range(n):
            if graph[i][j]==0:
                return 0
    return 1



def BFS_iter():

    global queue
    global tempQueue

    tempQueue=queue
    queue=deque()

    while tempQueue:
        x,y=tempQueue.popleft()

        for i in range(4):
            dx=x+dir[i][0]
            dy=y+dir[i][1]

            if dx<0 or dx>=m or dy<0 or dy>=n:
                continue

            if graph[dx][dy]==-1:
                continue

            if graph[dx][dy]==0:
                graph[dx][dy]=1
                queue.append((dx,dy))

count=0
while queue:
    BFS_iter()
    count+=1

if is_eqaul():
    print(count-1)
else:
    print(-1)
