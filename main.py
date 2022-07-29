import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
graph=list()
dir=[[-1,0],[1,0],[0,-1],[0,1]]

for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip()))

alpha=set()
alpha.add(graph[0][0])
ans=0

def dfs_recur(x,y,count):
    global ans
    ans=max(ans,count)

    for i in range(4):
        dx=x+dir[i][0]
        dy=y+dir[i][1]

        if dx>=0 and dx<n and dy>=0 and dy<m and graph[dx][dy] not in alpha:
            alpha.add(graph[dx][dy])
            dfs_recur(dx,dy,count+1)
            alpha.remove(graph[dx][dy])


dfs_recur(0,0,1)
print(ans)