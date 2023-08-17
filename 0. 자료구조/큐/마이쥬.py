# p = 1 #줄설 '첫번째' 사람번호
# q = [] #큐
# N = 200000 #마이쮸 개수 #1.251 1.256 1.314
# m = 0 #나눠준 개수

# while m < N:
#     q.append((p, 1, 0))
#     v, c, my = q.pop(0)
#     # print(f'큐에 남아있는 사람수{len(q)+1} 받아갈 사탕수{c} 나눠준 사탕수{m}')
#     m += c
#     q.append((v, c+1, my+c))
#     p += 1 #처음 줄서는 사람 번호
# print(f'마지막 사탕을 받은사람{v}')
"""#0.425 0.457 0.412
from collections import deque
p = 1 #줄설 '첫번째' 사람번호
q = deque() #큐
N = 200000 #마이쮸 개수 
m = 0 #나눠준 개수

while m < N:
    q.append((p, 1, 0))
    v, c, my = q.popleft()
    # print(f'큐에 남아있는 사람수{len(q)+1} 받아갈 사탕수{c} 나눠준 사탕수{m}')
    m += c
    q.append((v, c+1, my+c))
    p += 1 #처음 줄서는 사람 번호
print(f'마지막 사탕을 받은사람{v}')
"""
#함수화 0.46~0.52
def enQ(data):
    global rear
    # if rear == Qsize - 1:
    if Full():
        print("Queue full")
    rear += 1
    Q[rear] = data

def deQ():
    global front
    # if front == Qsize - 1:
    if isEmpty():
        print("Queue empty")
    else:
        front += 1
        return Q[front]

def isEmpty():
    global front
    global rear
    return front == rear

def Full():
    global front
    global rear
    return rear == len(Q) - 1

def Qpeek():
    global front
    if isEmpty():
        print("Queue empty")
    else:
        return Q[front+1]
p = 1 #줄설 '첫번째' 사람번호

N = 200000 #마이쮸 개수
m = 0 #나눠준 개수
Q = [0]*N*2 #큐
rear = -1
front = -1
Qsize = len(Q)


while m < N:
    enQ((p, 1, 0))
    v, c, my = deQ()
    # print(f'큐에 남아있는 사람수{len(q)+1} 받아갈 사탕수{c} 나눠준 사탕수{m}')
    m += c
    enQ((v, c+1, my+c))
    p += 1 #처음 줄서는 사람 번호
print(f'마지막 사탕을 받은사람{v}')


