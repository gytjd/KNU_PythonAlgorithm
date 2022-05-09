n, m = list(map(int, input().split()))
a, b, d = list(map(int, input().split()))

game_maps = []

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

count = 1
false_area = 0

for i in range(m):
  game_map = list(map(int, input().split()))
  game_maps.append(game_map)

while True:

  d = (d-1) % len(direction)

  da = a + direction[d][0]
  db = b + direction[d][1]


  if game_maps[da][db] == 0:
    game_maps[a][b] = 2
    a = da
    b = db
    count = count + 1
    false_area = 0

  false_area = false_area + 1
  
  if false_area == 4:  
    a = a + direction[(d-2)%4][0]  
    b = b + direction[(d-2)%4][1]  
    if(game_maps[a][b] == 1):  
      break  
  
  
  
print(count)