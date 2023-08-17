from queue import PriorityQueue

# q = PriorityQueue()
q = PriorityQueue(maxsize=8)

# 추가
q.put(1)
q.put(2)
q.put(3)
q.put(4)
# 뺴기
print(q.get())
print(q.get())
print(q.get())
print(q.get())

q.put((3, '윤태우'))
q.put((1, '황호철'))
q.put((2, '원종현'))
# 우선 순위로 들어감
q.put((0, '허범성'))

print(q.get()[1])
print(q.get())
print(q.get())
print(q.get())