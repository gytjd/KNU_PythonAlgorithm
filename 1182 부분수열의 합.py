import sys
from itertools import combinations

n,s=map(int,sys.stdin.readline().split())
array=list(map(int,sys.stdin.readline().split()))
result=list()

for i in range(1,n+1):
    result.append((combinations(array,i)))

count=0

for i in result:
    for j in i:
        if sum(j)==s:
            count+=1

print(count)

