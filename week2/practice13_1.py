#컨트롤 제트

def solution(s):
    answer = 0
    s_list = s.split(" ")
    for i in range(0, len(s_list)):
        if s_list[i]=="Z":
            answer-=int(s_list[i-1])
        else:
            answer+=int(s_list[i])
    return answer