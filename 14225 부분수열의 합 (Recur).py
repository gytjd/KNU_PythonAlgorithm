import sys

n=int(input())
array=list(map(int,sys.stdin.readline().split()))
result=list()

s=0
def subset(idx,a):
    if idx>=n:
        return


    a+=array[idx]
    result.append(a)

    subset(idx+1,a)
    subset(idx+1,a-array[idx])


subset(0,0)
max_num=max(result)
result.sort()
result=set(result)

resultB=set()
for i in range(1,max_num+1):
    resultB.add(i)

temp_result=resultB-result

if temp_result:
    print(min(temp_result))
else:
    print(max_num+1)