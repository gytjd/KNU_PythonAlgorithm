n, m = map(int, input().split())
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

max=min(data[0])
for i in range(1,n):
    if max<min(data[i]):
        max=min(data[i])

print(max)    