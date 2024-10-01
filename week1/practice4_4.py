#배열의 평균값

def solution(numbers):
    number_sum = 0
    for i in numbers:
        number_sum += i
    number_long = len(numbers)
    answer = number_sum/number_long
    return answer