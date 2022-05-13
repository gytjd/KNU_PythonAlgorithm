num=int(input())

ary=[0 for i in range(num)]
for i in range(num):
    ary[i]=input().split()

ary.sort()

for i in range(num):
    print(ary[i][0],end=' ')


