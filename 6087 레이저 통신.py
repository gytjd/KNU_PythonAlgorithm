import sys
from collections import deque

dir=[[0,1],[1,0],[0,-1],[-1,0]]

n,m=map(int,sys.stdin.readline().split())
graph=[list(sys.stdin.readline().rstrip())for i in range(m)]
dir_graph=[[0 for i in range(n)]for i in range(m)]
visited=[[0 for i in range(n)]for i in range(m)]


queue=deque()


def BFS_iter(x,y,direction):

    queue.append((x,y,direction))
    visited[x][y]=1
    graph[x][y]=0

    while queue:
        x,y,z_direction=queue.popleft()

        if x==endA and y==endB:
            print(dir_graph[x][y])
            break

        for i in range(4):
            dx=x+dir[i][0]
            dy=y+dir[i][1]
            temp_direction=i


            if dx<0 or dx>=m or dy<0 or dy>=n:
                continue

            if graph[dx][dy]=="*":
                continue
            else:
                if visited[dx][dy]==0:
                    visited[dx][dy]=1
                    graph[dx][dy]=graph[x][y]+1

                    if graph[x][y]>=1:
                        if z_direction!=temp_direction:
                            dir_graph[dx][dy]=dir_graph[x][y]+1
                            queue.append((dx, dy, temp_direction))
                        else:
                            dir_graph[dx][dy]=dir_graph[x][y]
                            queue.appendleft((dx,dy,temp_direction))
                        continue

                    queue.append((dx, dy, temp_direction))
                else:
                    if graph[x][y]>=1:
                        if z_direction!=temp_direction:
                            dir_graph[dx][dy]=min(dir_graph[x][y]+1,dir_graph[dx][dy])
                        else:
                            dir_graph[dx][dy]=min(dir_graph[x][y],dir_graph[dx][dy])



for i in range(m):
    for j in range(n):
        if graph[i][j]=="C":
            queue.append((i,j,0))

startA,startB,startDir=queue.popleft()
endA,endB,endDir=queue.popleft()


BFS_iter(startA,startB,0)

for i in dir_graph:
    print(i)
