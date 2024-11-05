#연속된 수의 합

def solution(num, total):
    answer = []
    d=0
    for i in range(1, num):
        d += i
    start=(total-d)/num
    for i in range(start, start+num):
        answer.append(i)
    return answer