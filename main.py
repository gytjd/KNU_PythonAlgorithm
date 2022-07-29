import sys

n=int(input())
array=list(map(int,sys.stdin.readline().split()))
result=list()

def subset(idx):
    if len(array)==2:
        result.append(idx)
        return

    for i in range(1,len(array)-1):
        a=array[i-1]*array[i+1]
        temp=array[i]
        del array[i]
        subset(idx+a)
        array.insert(i,temp)



subset(0)
print(result)


