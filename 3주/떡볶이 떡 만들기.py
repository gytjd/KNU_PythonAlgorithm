N,M=map(int,input().split())
a=list(map(int,input().split()))

def find_maxheight(ary,height,size):
    sum=0
    for i in range(size):
        if ary[i]-height<0:
            continue
        else:
            sum+=ary[i]-height
    return sum


for i in range(max(a),min(a)-1,-1):
    if find_maxheight(a,i,N)==M:
        print(i)
        break

        

