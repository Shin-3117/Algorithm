#초기 공백 상태
front = rear = 0

#index 순환 -> front와 rear가 배열의 마지막 인덱스인 n-1을 가리킨 후
#그다음 0으로이동해야함 -> 나머지 연산자 mod 사용
#기존에 mod n만 추가한다고 생각


# 원형 큐
def enq(data):
    global rear
    global front
    # if (rear+1) % cQsize == front:
    #     print("cQ is Full")
    if (rear+1) % cQsize == front:
        front = (front+1) % cQsize
    #Queue가 가득찼을때 덮어쓰기
    else:
        rear = (rear + 1) % cQsize
        cQ[rear] = data

def deq():
    global front
    front = (front + 1) % cQsize
    return cQ[front]


cQsize = 4
cQ = [0] * cQsize
front = 0
rear = 0


enq(1)
enq(2)
enq(3)
enq(4)
enq(5)
print(deq())
print(deq())
print(cQ)