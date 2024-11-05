#n의 배수 구하기

def solution(n, numlist):
    answer = []
    for i in numlist:
        if(i%n==0):
            answer.append(i)
    return answer