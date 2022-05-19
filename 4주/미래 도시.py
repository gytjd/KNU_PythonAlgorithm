N,M=map(int,input().split())
graph = [[1000]*(N+1) for _ in range(N+1)]

visited = [0]*(N+1)
distance = [0]*(N+1)

for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
X, K = map(int, input().split())
    
    
def display_graph(n):
    for i in range(1,N+1):
        for j in range(1,N+1):
            print(graph[i][j],end="   ")
        print()


def display_distance(n):
    for i in range(1,N+1):
        print(distance[i],end="   ")
    print()
        
def find_minDis(n):
    min = 1000
    minpos=0
    
    for i in range(1, N+1):
        if visited[i] == 0 and min > distance[i]:
            min=distance[i]
            minpos = i
            break;

    return minpos


def Dijkstra(graph,n):
    
    visited[n] = 1
    for i in range(1, N+1):
        distance[i] = graph[n][i]

    for i in range(1, N+1):

        u = find_minDis(N)
        visited[u] = 1

        for j in range(1, N+1):
            if visited[j] == 0:
                if distance[j] > distance[u]+graph[u][j]:
                    distance[j] = distance[u]+graph[u][j]
        

Dijkstra(graph,1)

if graph[K][X]==1:
    print(distance[K]+1)
else:
    print("-1")
    



    
    
