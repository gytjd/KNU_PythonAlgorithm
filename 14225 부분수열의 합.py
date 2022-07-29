import sys
from itertools import combinations

n=int(input())
array=list(map(int,sys.stdin.readline().split()))
result=list()

for i in range(1,n+1):
    result.append(combinations(array,i))

print(result)