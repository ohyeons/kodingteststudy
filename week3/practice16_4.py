#배열의 유사도

def solution(s1, s2):
    answer = 0
    for i in range(len(list(s1))):
        for j in range(len(list(s2))):
            if s1[i]==s2[j]:
                answer+=1
    return answer
