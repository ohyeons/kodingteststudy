#숨어있는 숫자의 덧셈(2)

def solution(my_string):
    for i in my_string:
        if i.isalpha():
            my_string = my_string.replace(i, ' ')
    my_string = my_string.split()
    
    return sum(list(map(int, my_string)))