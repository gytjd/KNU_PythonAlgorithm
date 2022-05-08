data=input();
row=int(data[1])-1;
col=int(ord(data[0])-ord('a'));


move=[[0 for j in range(2) for i in range(8)]]
move = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [1, -2], [1, 2], [-1, 2]];

result=0;

for i in range(8):
    next_row = move[i][0]+row;
    next_col=move[i][1]+col;
        
    if next_row>=0 and next_col<=8 and next_col>=0 and next_col<=8:
        result+=1;


print(result)