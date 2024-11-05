#숫자 찾기

def solution(num, k):
    
    list_num = list(str(num))
    
    for i in range(len(list_num)):
        if(list_num[i]==str(k)):
                   return i+1
    return -1