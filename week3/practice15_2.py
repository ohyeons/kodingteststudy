#인덱스 바꾸기

def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    a = my_string[num1]
    my_string[num1] = my_string[num2]
    my_string[num2] = a
    
    for i in my_string:
        answer += i
        
    return answer