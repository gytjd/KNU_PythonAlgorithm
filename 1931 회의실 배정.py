import sys

n=int(input())
conf=[[0]*2 for i in range(n)]

for i in range(n):
    start,end=map(int,sys.stdin.readline().split())
    conf[i][0]=start
    conf[i][1]=end

conf.sort(key=lambda x:(x[1],x[0]))

end=conf[0][1]
count=1
for i in range(1,n):
    if conf[i][0]>=end:
        count+=1
        end=conf[i][1]

print(count)