def solution(nums):
    answer = 0
    pick_num = len(nums)//2
    only_num = len(set(nums))
    if pick_num > only_num: return only_num
    return pick_num

a1 = solution([3,1,2,3])
print(a1)
a2 = solution([3,3,3,2,2,4])
print(a2)
a3 = solution([3,3,3,2,2,2])
print(a3)