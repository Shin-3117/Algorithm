""" 내장 함수 사용
from collections import deque
q = deque()
q.append('a')
q.append('b')
print(q)
print(q.popleft())
print(q.popleft())
"""
""" 리스트로 구현
Q = []
#추가
Q.append('a')
Q.append('B')
print(Q)
#삭제
print(Q.pop(0))
print(Q.pop(0))
"""
""" front, rear로 구현
queue = [0] * 100
front = -1
rear = -1

rear += 1
queue[rear] = 'a'
rear += 1
queue[rear] = 'b'
print(queue)

front += 1
print(queue[front])
front += 1
print(queue[front])
"""
#함수화
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

Q = [0] * 3
Qsize = len(Q)
rear = -1
front = -1

enQ(1)
enQ(2)
enQ(3)

print(deQ())
print(deQ())
print(Qpeek())