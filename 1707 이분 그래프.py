import sys

from collections import deque

k = int(input())


def BFS_queue(first):
    Color[first]="B"
    visited[first] = 1
    queue=deque()
    queue.append(first)

    while queue:
        v = queue.popleft()
        visited[v] = 1

        if Color[v] == 'B':
            for i in graph[v]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1

                if Color[i] == "B":
                    return 0
                else:
                    Color[i] = "R"
        else:
            for i in graph[v]:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i]=1

                if Color[i] == "R":
                    return 0
                else:
                    Color[i] = "B"
    return 1


for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = [[] for i in range(v + 1)]
    visited = [0 for i in range(v + 1)]
    result = set()

    for _ in range(e):
        start, end = map(int, sys.stdin.readline().split())
        graph[start].append(end)
        graph[end].append(start)
        result.add(start)
        result.add(end)

    for i in result:
        Color = ["" for i in range(v + 1)]

        if BFS_queue(i) == 0:
            print("NO")
            break
    else:
        print("YES")