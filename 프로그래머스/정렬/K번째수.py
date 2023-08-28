def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]-1
        end = command[1]
        pick = command[2]-1
        # i,j,k = command
        # 이런식으로 한번에 받을 수 있음(갯수 정해저있으면)
        cnt=[]
        cnt = array[start:end]
        cnt.sort()
        answer.append(cnt[pick])
    return answer