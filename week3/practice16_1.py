#편지

def solution(message):
    answer = 0
    message = list(message)
    for i in range(0,len(message)):
        answer += 1
    result = answer*2
    return result