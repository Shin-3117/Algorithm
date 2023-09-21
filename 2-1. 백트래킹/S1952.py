# [모의 SW 역량테스트] 수영장
import sys
sys.stdin = open('inputs2/S1952.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    # 1일, 1달, 3달, 1년
    tickets = list(map(int, input().split()))
    plans = list(map(int, input().split()))
    oneMonths = []
    oneYear = tickets[3]
    # 1달 단위로 가장 저렴한 요금 
    for i in plans:
        oneMonths.append(min(tickets[1], i*tickets[0]))

    # 1+2+3달요금 - 3달요금 리스트
    one3Months = []
    for i in range(-2,12):
        start = i if i >= 0 else 0
        end = i + 3 if i + 3 < 12 else 12
        one3Month = 0
        for j in range(start, end):
            one3Month += oneMonths[j]
        if one3Month > tickets[2]:
            one3Months.append(one3Month-tickets[2])
        else: one3Months.append(0)
    # 배열을 추가하며 3달 요금으로 할인 되는 금액 총합 구하기
    sales = [one3Months[0], one3Months[1], one3Months[2]]
    for i in range(3,14):
        if sales[i-1] > sales[i-3] + one3Months[i]:
            sales.append(sales[i-1])
        else: sales.append(sales[i-3] + one3Months[i])

    sol = sum(oneMonths) - sales[-1]
    if sol > oneYear:
        sol = oneYear
    print(f'#{tc} {sol}')

"""
def func(val,idx):
    global res
    if idx>=12:
        res=min(res,val)
        return
    if val>res:
        return
    func(val+A[idx],idx+1)
    func(val+b,idx+1)
    func(val+c,idx+3)
 
for m in range(int(input())):
    a,b,c,d=map(int,input().split())
    plan=list(map(int,input().split()))
    A=[a*i for i in plan]
    res=d
    func(0,0,)
    print(f'#{m+1} {res}')
"""