import sys
sys.stdin = open('./SW_TEST/P_A6.txt','r')

for testCase in range(int(input())):
    sol = 0
    numberOfTree = int(input())
    treesHigh = list(map(int,input().split()))

    targetHigh = max(treesHigh)
    to_grow_tree_list = []
    for treeHigh in treesHigh:
        if targetHigh-treeHigh != 0:
            to_grow_tree_list.append(targetHigh-treeHigh)
    
    for tree in to_grow_tree_list:
        sol +=1
        

    print(f'#{testCase+1} {sol}')