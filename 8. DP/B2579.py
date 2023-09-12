N = int(input())
steps = [int(input()) for _ in range(N)]
data = [0]*N
if N<=1:
    print(steps[0])
else:
    data[0] = steps[0]
    data[1] = steps[1] + steps[0]
    # print(data)
    for i in range(2,N):
        data[i] = max(data[i-2]+steps[i], data[i-3]+steps[i-1]+steps[i] )
    print(data[N-1])