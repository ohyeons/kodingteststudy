#구슬을 나누는 경우의 수

def solution(balls, share):
    answer1 = 1
    answer2 = 1
    answer3 = 1
    
    for i in range(1,balls+1):
        answer1 *= i
    for j in range(1,share+1):
        answer2 *= j
    for k in range(1,balls-share+1):
        answer3 *= k
    result = answer1/(answer2*answer3)
    
    return result