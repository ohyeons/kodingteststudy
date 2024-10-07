#최댓값 구하기(1)

def solution(numbers):
    numbers = sorted(numbers)
    answer = numbers[-1]*numbers[-2]
    return answer