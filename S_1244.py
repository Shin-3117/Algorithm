# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금
import sys
sys.stdin = open('./inputs/S_1244.txt','r')
"""
숫자판의 정보는 정수형 숫자로 주어지고 최대 자릿수는 6자리이며, 
최대 교환 횟수는 10번이다
"""
for t in range(int(input())):
    nums, change_count = input().split()
    change_count = int(change_count)
    nums = list(map(int,nums.strip()))
    # print(nums, change_count)
    sorted_nums = sorted(nums,reverse=True)
    # print(sorted_nums)
    for change in range(change_count):
        if nums == sorted_nums:
            # 중복되는 숫자가 없는 경우 1의자리 10의 자리 교체
            if len(list(set(nums))) == len(nums):
                cnt = nums[-1]
                nums[-1] = nums[-2]
                nums[-2] = cnt
                continue
        for i in range(len(nums)):
            # 교환 대상 찾기 및 교환
            if nums[i] == sorted_nums[i]:
                continue
            else:
                cnt = nums[i]
                # 교환 횟수가 남아있고, 가장 큰 수가 중복될 때
                left_change = change_count - change
                for j in range(len(nums)):
                    if sorted_nums[i] == nums[-j-1]:
                        change_idx = -j-1
                        if left_change ==1:
                            break
                        left_change -= 1
                nums[i] = nums[change_idx]
                nums[change_idx] = cnt
                break
    sol = ''
    for i in nums:
        sol += str(i)
    print(f'#{t+1} {sol}')
