
N,M=map(int,input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))
    
move = [[0 for j in range(2) for i in range(4)]]
move=[[-1,0],[0,-1],[1,0],[0,1]]

def count_ice(i,j):
    
    if i<=-1 or i>=N or j<=-1 or j>=M:
        return
    else:
        
        if graph[i][j]==0:
            
            graph[i][j]=1;
                 
            for x in range(4):
                count_ice(move[x][0]+i,move[x][1]+j)
            
            return True
        else:
            return False
        
    
    
        
result=0

for i in range(N):
    for j in range(M):
        
        if count_ice(i,j)==True:
            result+=1

print(result)
        

