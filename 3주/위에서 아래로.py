num=int(input())

ary = [0 for i in range(num)]

for i in range(num):
    ary[i]=int(input())

ary.sort(reverse=True)
for i in range(num):
    print(ary[i],end=' ')
