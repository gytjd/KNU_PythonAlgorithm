import sys


def check_row(x,a):
    for i in range(9):
        if sdoku[x][i]==a:
            return 0
    return 1

def check_col(y,a):
    for i in range(9):
        if sdoku[i][y]==a:
            return 0
    return 1

def check_square(x,y,a):
    dx=x//3*3
    dy=y//3*3

    for i in range(dx,dx+3):
        for j in range(dy,dy+3):
            if sdoku[i][j]==a:
                return 0
    return 1

def check_total(x,y,a):
    if check_row(x, a) and check_col(y, a) and check_square(x, y, a):
        return 1
    return 0


def display_sdoku():
    for i in sdoku:
        print(*i)
    print()

def all_sdoku():
    for i in sdoku:
        for j in i:
            if j==0:
                return 0
    return 1

def complete_sdoku(zero_count):
    if all_sdoku()==4:
        display_sdoku()
        return



    for i in tempA:
        nx=temp_zero[zero_count][0]
        ny=temp_zero[zero_count][1]

        for j in range(4):
            qx=nx+dir[j][0]
            qy=ny+dir[j][1]

            if qx<0 or qx>8 or qy<0 or qy>8:
                continue

            if sdoku[qx][qy]==0:
                if check_total(nx,ny,i[0]) and check_total(qx,qy,i[1]):
                    sdoku[nx][ny] = i[0]
                    sdoku[qx][qy] = i[1]
                    complete_sdoku(zero_count + 1)
                    sdoku[nx][ny] = 0
                    sdoku[qx][qy] = 0



while True:
    n=int(input())

    if n==0:
        break
    dir=[[0,1],[1,0],[0,-1],[-1,0]]

    tempA=list()
    for i in range(1,10):
        for j in range(1,10):
            if i==j:
                continue
            else:
                tempA.append((i, j))



    sdoku=[[0 for i in range(9)]for i in range(9)]
    for i in range(n):
        temp=sys.stdin.readline().split()
        sdoku[ord(temp[1][0])-65][int(temp[1][1])-1]=int(temp[0])
        sdoku[ord(temp[3][0]) - 65][int(temp[3][1])-1] = int(temp[2])
        tempA.remove((int(temp[0]), int(temp[2])))
        tempA.remove((int(temp[2]), int(temp[0])))

    temp=sys.stdin.readline().split()
    for i in range(len(temp)):
        sdoku[ord(temp[i][0])-65][int(temp[i][1])-1]=i+1

    temp_zero=list()

    for i in range(9):
        for j in range(9):
            if sdoku[i][j]==0:
                temp_zero.append((i,j))

    complete_sdoku(0)

