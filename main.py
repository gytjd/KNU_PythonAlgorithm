import sys
from itertools import combinations

n = int(input())

result=list()

for _ in range(n):
    result.append(list(map(int,sys.stdin.readline().split())))


temp = [i for i in range(1, n + 1)]
temp = list(combinations(temp, n // 2))


sum=100

for i in range(len(temp) // 2):
    j = i
    k = len(temp) - i - 1

    tempStart = 0
    tempLink = 0

    for startA in temp[j]:
        for startB in temp[j]:
            tempStart+=result[startA-1][startB-1]

    for linkA in temp[k]:
        for linkB in temp[k]:
            tempLink+=result[linkA-1][linkB-1]

    sum=min(sum,abs(tempStart-tempLink))


print(sum)