import sys

n,m=map(int,sys.stdin.readline().split())
friend=[list() for i in range(n)]

for _ in range(m):
    start,end=map(int,sys.stdin.readline().split())
    friend[start].append(end)
    friend[end].append(start)

def DFS_recur(first,idx):

    visited[first]=1

    if idx==4:
        print(1)
        exit()

    for i in friend[first]:
        if visited[i]==0:
            DFS_recur(i,idx+1)
            visited[i]=0

for i in range(n):
    visited = [0 for i in range(n)]
    DFS_recur(i,0)
print(0)