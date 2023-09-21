
talls = []
for _ in range(9):
    talls.append(int(input()))
# print(talls)
talls.sort()
cnt =[]
sol = []
def back(s):
    if len(sol) == 7: return
    if len(cnt) == 7:
        print(cnt)
        tall_sum = 0
        for i in cnt:
            tall_sum += talls[i]
        if tall_sum == 100:
            for i in cnt:
                sol.append(talls[i])
            return
        return
    for i in range(s, 9):
        if i not in cnt:
            cnt.append(i)
            back(i+1)
            cnt.pop()
back(0)
# print(sol)

for i in sol:
    print(i)
