#주사위의 개수

def solution(box, n):
    width = box[0]//n
    length = box[1]//n
    height = box[2]//n
    answer = width*length*height
    return answer