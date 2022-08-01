import sys
from collections import deque

dir=[[0,1],[1,0],[0,-1],[-1,0]]

n=int(sys.stdin.readline())
mapGraph=[list(sys.stdin.readline().rstrip()) for i in range(n)]

visited=[[0 for i in range(n)]for i in range(n)]
RGvisited=[[0 for i in range(n)]for i in range(n)]


def BFS_iter(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        dx,dy=queue.popleft()

        for i in range(4):
            nx=dx+dir[i][0]
            ny=dy+dir[i][1]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if mapGraph[dx][dy] == "R" or mapGraph[dx][dy] == "G":
                    if visited[nx][ny] == 0 and (mapGraph[nx][ny] == "R" or mapGraph[nx][ny] == "G"):
                        visited[nx][ny] = 1
                        queue.append((nx, ny))

                elif mapGraph[dx][dy] == "B":
                    if visited[nx][ny] == 0 and mapGraph[nx][ny] == "B":
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
    return 1


def BFS_normal(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        dx,dy=queue.popleft()

        for i in range(4):
            nx=dx+dir[i][0]
            ny=dy+dir[i][1]

            if nx>=0 and nx<n and ny>=0 and ny<n:
                if mapGraph[dx][dy] == mapGraph[nx][ny]:
                    if RGvisited[nx][ny] == 0:
                        RGvisited[nx][ny] = 1
                        queue.append((nx, ny))
    return 1

rgcount=0
count=0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and BFS_iter(i,j)==1:
            visited[i][j]=1
            count+=1
        if RGvisited[i][j]==0 and BFS_normal(i,j)==1:
            RGvisited[i][j]=1
            rgcount+=1

print(rgcount,count)
