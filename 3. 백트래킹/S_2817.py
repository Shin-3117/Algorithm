# 2817. 부분 수열의 합
import sys
sys.stdin = open('./inputs/S_2817.txt','r')

def backTracking(start,sum_value):
    global sol
    if sum_value == target: 
        sol +=1
        return
    elif sum_value > target: 
        return
    for i in range(start,total_nums):
        sum_value += nums[i]
        backTracking(i+1,sum_value)
        sum_value -= nums[i]


total_test_case_num = int(input())
for test_case in range(total_test_case_num):
    total_nums, target = map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort(reverse=True)
    sol = 0
    backTracking(0,0)
    print(f'#{test_case+1} {sol}')