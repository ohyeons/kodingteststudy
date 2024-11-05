#OX퀴즈

def solution(quiz):
    answer = []
    for j in quiz:
        split_quiz =j.split()
        if split_quiz[1]=='+':
            if int(split_quiz[0])+int(split_quiz[2])==int(split_quiz[4]):
                answer.append('O')
            else:
                answer.append('X')
        elif split_quiz[1]=='-':
            if int(split_quiz[0])-int(split_quiz[2])==int(split_quiz[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer