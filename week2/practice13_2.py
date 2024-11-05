#배열 원소의 길이

def solution(strlist):
    answer = []
    for i in range(0, len(strlist)):
        answer.append(len(strlist[i]))
    return answer