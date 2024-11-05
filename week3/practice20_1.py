#직사각형의 넓이 구하기

def solution(dots): 
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    
    w = max(x) - min(x)
    h = max(y) - min(y)
    area = w*h
    return area