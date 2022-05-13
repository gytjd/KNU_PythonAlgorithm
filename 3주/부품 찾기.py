N=int(input())
a=list(map(int,input().split()))
M=int(input())
b=list(map(int,input().split()))

def seq_search(ary,num,size):
    for i in range(size):
        if ary[i]==num:
            return 1
    
    return 0

for i in range(M):
    if seq_search(a,b[i],N)==1:
        print("yes",end=" ")
    else:
        print("no",end=" ")

