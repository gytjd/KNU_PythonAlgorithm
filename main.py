import sys

n,m=map(int,sys.stdin.readline().split())
graph=[list(sys.stdin.readline().rstrip())for i in range(n)]

row_count=0
for i in graph:
    if "X" not in i:
        row_count+=1

col_count=0
for i in range(m):
    for j in range(n):
        if graph[j][i]=="X":
            break
    else:
        col_count+=1

if row_count==0 or col_count==0:
    if row_count==0:
        print(col_count)
    else:
        print(row_count)
else:
    if row_count>=col_count:
        print(row_count)
    else:
        print(col_count)

