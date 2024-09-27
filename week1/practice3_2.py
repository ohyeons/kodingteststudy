#중앙값 구하기

def solution(array):
    array = sorted(array)
    num = len(array)
    mid_num = num//2
    
    answer = array[mid_num]
    return answer