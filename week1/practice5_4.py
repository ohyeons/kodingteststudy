#배열 뒤집기

def solution(num_list):
    answer = []
    for i in range(len(num_list)):
        number = num_list[len(num_list)-(i+1)]
        answer.append(number)
    return answer