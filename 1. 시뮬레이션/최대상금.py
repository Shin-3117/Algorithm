T = int(input())
for t in range(1, T+1):
    numbers, count = input().split()
    # print(numbers,count)
    count = int(count)

    # print(set(numbers))
    # print(set([numbers]))
    nums = set([numbers])
    SET = set()

    for k in range(count):
        while nums:
            n = nums.pop()
            n = list(n)
            for i in range(len(numbers)):
                for j in range(i + 1, len(numbers)):
                    # print(i,j)
                    # print(n[i], n[j])
                    n[i], n[j] = n[j], n[i]
                    SET.add(''.join(n))
                    # print('set',SET,k,i,j)
                    n[i], n[j] = n[j], n[i]
        # print('before',nums,SET)
        nums, SET = SET, nums
        # print('after',nums,SET)
        # 모든 교체하는 경우의 수 (중복은 set으로 제거)

    result = max(nums)
    print(f'#{t} {result}')