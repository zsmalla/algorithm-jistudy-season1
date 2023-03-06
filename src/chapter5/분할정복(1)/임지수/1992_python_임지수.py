import sys

input = sys.stdin.readline

def quadtree():
    answer = ''

    def recur(image):
        nonlocal answer
        
        # for i in range(len(image)):     # for test
        #     print(*image[i])            

        if len(image) != 2:
            half = len(image)//2

            for i in range(2):        
                for j in range(2):     
                    answer += '(' + recur([[image[i*half + r][j*half + c] for c in range(half)] for r in range(half)]) + ')'

        else:
            # for i in range(len(image)):
            #     print(*image[i], '\n')
            flat = [image[i][j] for i in range(2) for j in range(2)]
            if flat.count('0') == 4:
                return '0'
            elif flat.count('1') == 4:
                return '1'
            else:
                return '('+''.join(flat)+')'
        
        return ''
            
    recur(_image)
    return answer 

N = int(input().rstrip())
_image = [list(input().rstrip()) for _ in range(N)]
print(quadtree())