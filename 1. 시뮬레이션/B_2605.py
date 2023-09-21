N = int(input())
L = list(map(int, input().split()))
sol = []
for i in range(N):
    sol.insert(len(sol)-L[i], i+1)
print(*sol)