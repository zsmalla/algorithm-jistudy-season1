import sys

input = sys.stdin.readline

def quadtree(r, c, n):
    
    check = image[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if image[i][j] != check:
                check = -1
                break
            
    if check == -1:
        print("(", end='')
        n //= 2
        quadtree(r, c, n)
        quadtree(r, c + n, n)
        quadtree(r + n, c, n)
        quadtree(r + n, c + n, n)
        print(")", end='')
    elif check == 1:
        print('1', end ='')
    else:
        print('0', end = '')
    
N = int(input().rstrip())
image = [list(map(int, input().rstrip())) for _ in range(N)]
quadtree(0, 0, N)
