from heapq import heappush, heappop

arr = [20, 15, 19, 4, 13, 11]

# 최소힙
min_heap = []

for el in arr:
    heappush(min_heap, el)

print(min_heap)  # [4, 13, 11, 20, 15, 19] 출력

while len(min_heap) > 0:
    print(heappop(min_heap), end=' ')
print()

# 최대힙
max_heap = []
for el in arr:
    heappush(max_heap, -el)

print(max_heap)  # [-20, -15, -19, -4, -13, -11] 출력

while len(max_heap) > 0:
    print(-heappop(max_heap), end=' ')


