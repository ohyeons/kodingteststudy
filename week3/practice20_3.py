#최댓값 구하기(2)

def solution(numbers):
    numbers.sort(reverse = True)
    return max(numbers[0] * numbers[1],numbers[-1] * numbers[-2])