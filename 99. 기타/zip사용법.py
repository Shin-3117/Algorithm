
data = [[0,1,2],[10,11,12],[20,21,22]]
for i in data:
    print(i)

r0 = list(zip(*data))
for i in r0:
    print(i)