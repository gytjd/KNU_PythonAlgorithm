N,M,K=map(int,input().split())
ary=list(map(int,input().split()))

ary.sort()
ary.reverse()



k=0
sum=0
count=0


while count<M:
    if(ary[k]!=ary[k+1]):
        for j in range(K or count<=M):
            sum+=ary[k]
            count+=1
        if(count>=M):
            break; 
        sum+=ary[k+1]
        count+=1
    else:
        for j in range(K or count<=M):        
            sum+=ary[k]
            count+=1
        for j in range(K or count<=M):
            sum+=ary[k+1]
            count+=1
        
            
        
        
print(sum)  
