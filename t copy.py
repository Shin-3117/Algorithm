def choose(n,k):
    if k == 0: 
       return 1
    elif n < k:
       return 0
    else:
        return choose(n-1, k-1) + choose(n-1, k)

print(choose(10,2))