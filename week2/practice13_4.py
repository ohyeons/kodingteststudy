#삼각형의 완성 조건(1)

def solution(sides):
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        answer = 1
    else:
        answer = 2
    return answer