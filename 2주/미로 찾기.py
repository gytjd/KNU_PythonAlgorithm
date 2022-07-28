n,m=map(int,input().split())

maze = []
for i in range(n):
    maze.append(list(map(int, input())))

mark = [[0 for j in range(m)] for i in range(n)]
    

move = [[0 for j in range(2) for i in range(4)]]
move=[[-1,0],[0,1],[1,0],[0,-1]]


count=0

def find_maze(i,j):
    global count
    mark[i][j]=1
    
    if i==n-1 and j==m-1:
        print(count+1)
        return
    else:
        
        for k in range(4):
            next_row = move[k][0]+i
            next_col = move[k][1]+j
            
            if(next_row<=-1 or next_row>=n or next_col<=-1 or next_col>=m):
                continue
                
            else:
                if maze[next_row][next_col]==1 and mark[next_row][next_col]==0:
                    count += 1
                    find_maze(next_row, next_col)
                    count-=1
                else:
                    continue

find_maze(0,0)
            
            
    
