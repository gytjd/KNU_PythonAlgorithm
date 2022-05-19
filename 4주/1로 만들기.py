N = int(input())

count = 0

while N != 1:
    if N > 5:
        if N % 5 == 0:
             N /= 5
             count += 1
        else:
            N -= 1
            count += 1
    else:
        if N % 2 == 0:
            while N != 1:
                N /= 2
                count += 1
        else:
            while N != 1:
                N /= 3
                count += 1


print(count)
