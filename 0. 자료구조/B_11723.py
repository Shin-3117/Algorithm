import sys
sys.stdin = open('./inputs2/B_11723.txt','r')
input = sys.stdin.readline
data = set()
for _ in range(int(input())):
    order = input().strip()
    try:
        a,b = order.split()
        # print(a,b)
        if a == 'add':
            data.add(b)
        elif a=='remove':
            data.remove(b)
        elif a=='check':
            if b in data:
                print(1)
            else: print(0)
        elif a=='toggle':
            if b in data:
                data.remove(b)
            else:
                data.add(b)
    except:
        # print(order)
        if order == 'all':
            data = set(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
            # print(list(data))
        elif order == 'empty':
            data = set()
            # print(list(data))