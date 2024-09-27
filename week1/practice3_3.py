#최빈값 구하기

def solution(array):
    reset = [0]*1001
    for num in array:
        reset[num]+=1
    answer = reset.index(max(reset))
    if reset.count(max(reset))>1:
        answer = -1
    return answer