import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]    #각 층마다 방문여부 저장 리스트
queue = deque()

dr = [-1,1,0,0]    #상하좌우
dc = [0,0,-1,1]

def bfs(x,y,z):
    queue.append([x,y,z])
    visited[x][y][z] = 1    #시작점 포함이므로 1
    while queue:
        X,Y,Z = queue.popleft()

        if X == N-1 and Y == M-1:    #도착시에 print -> exit
            print(visited[X][Y][Z])
            exit(0)

        for i in range(4):
            NX = X+dr[i]
            NY = Y+dc[i]
            #범위안에있고
            if 0<=NX<N and 0<=NY<M:
                #벽이 아니고 방문한적이 없다면
                if graph[NX][NY] == 0 and visited[NX][NY][Z] == 0:
                    visited[NX][NY][Z] = visited[X][Y][Z] + 1
                    queue.append([NX,NY,Z])
                #벽이고 부술 수 있는 횟수가 남아있고 부순후에 지점을 방문한적이 없다면
                elif Z > 0 and visited[NX][NY][Z-1] == 0:
                    visited[NX][NY][Z-1] = visited[X][Y][Z] + 1    #부순 후 레이어에 방문횟수 증감
                    queue.append([NX,NY,Z-1])    #부순 레이어로 이동 -> (Z-1)
bfs(0,0,1)    #시작 x, 시작 y, 부술 수 있는 횟수