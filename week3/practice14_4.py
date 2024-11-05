#대문자와 소문자

def solution(my_string):
    answer = ''
    for i in my_string:
        if ord(i)>=65 and ord(i)<=90:
            answer+=chr(ord(i)+32)
        elif ord(i)>=97 and ord(i)<=122:
            answer+=chr(ord(i)-32)
    return answer