#369게임

def solution(order):
    answer = 0
    str_order = str(order)
    split_order = list(str_order)
    for i in split_order:
        if i=='3'or i=='6' or i=='9':
            answer+=1
            
    return answer