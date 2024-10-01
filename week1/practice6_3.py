#짝수 홀수 갯수

def solution(num_list):
    d=0
    s=0
    
    for i in num_list:
        if i%2==0:
            d+=1
        else:
            s+=1
    answer = [d,s]
    return answer