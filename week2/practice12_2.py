#문자열 정렬하기(1)

def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
    answer = sorted(answer)
    return answer