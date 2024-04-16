#TRIANGLE
for i in range(4):
    for j in range(4-i-1):
        print(' ',end='')
    for k in range(2*i+1):
        print('*',end='')
    print()