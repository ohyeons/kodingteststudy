#영어가 싫어요

def solution(numbers):
    replace_numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for i in replace_numbers.keys():
        numbers = numbers.replace(i, replace_numbers[i])

    return int(numbers)