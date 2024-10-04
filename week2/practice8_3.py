#진료 순서정하기

def solution(emergency):
    answer = []
    example = []
    
    example = sorted(emergency)
    example.reverse()
    
    for i in emergency:
        answer.append(example.index(i)+1)
    return answer