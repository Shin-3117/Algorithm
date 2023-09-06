formula_lst = input().split('-')
# print(formula_lst)

num_lst = []
for i in formula_lst:
    nums = sum(map(int,i.split('+')))
    num_lst.append(nums)
# print(num_lst)
sol = num_lst[0]*2 -sum(num_lst)
print(sol)