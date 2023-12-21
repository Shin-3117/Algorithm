n = int(input())
Xn = list(map(int, input().split()))
setXn = sorted(set(Xn))
newXn = {setXn[i]:i for i in range(len(setXn))}

for i in Xn:
    print(newXn[i], end=' ')