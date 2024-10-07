#점의 위치 구하기

def solution(dot):
    i,j = dot
    if i>0 and j>0:
        answer = 1
    elif i>0 and j<0:
        answer = 4
    elif i<0 and j>0:
        answer = 2
    else:
        answer = 3
        
    return answer