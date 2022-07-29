import sys
from itertools import combinations

n=int(input())
array=list(map(int,sys.stdin.readline().split()))
result=list()

for i in range(1,n+1):
    result.append(combinations(array,i))

tempA=list()
for i in result:
    for j in i:
        tempA.append(sum(j))

tempA.sort()
tempA=set(tempA)
max_temp=max(tempA)

tempB=set()
for i in range(1,max_temp+1):
    tempB.add(i)

temp_result=tempB-tempA

if len(temp_result)==0:
    print(max_temp+1)
else:
    print(min(temp_result))


