#A를 B로 만들기

def solution(before, after):
    if sorted(before)==sorted(after):
        answer=1
    else:
        answer=0
    
    return answer