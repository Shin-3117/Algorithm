"""
(1 ≤ M ≤ N ≤ 8)
중복이 가능한 경우 : N^N, N=8 까지 가능
8^8 = 1677,7216
"""

import sys
N,M = map(int, sys.stdin.readline().split())

s = []

def back(start):
    # 선택해야 하는 수(M) 만큼 선택 후, 리턴
    if len(s) == M:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,N+1):
        if i not in s:
            s.append(i)
            back(i+1)
            s.pop()
back(1)
"""
만약 n=3, m=2라면 밑과 같은 형태로 진행될 것이다.
back(1){ 
    for문 i =1~3 i =1
    s : [1]

        back(2){ for문 i = 2~3
            s : [1,2]

            back(3){ for문 i = 3~3
                길이가 2이므로 print : (1 2)
                }
            
            s.pop()
            #s : [1]
        }
        back(3){ for문 i = 3~3
            s : [1,3]

            back(4){ for문 i = 4~3
                길이가 2이므로 print : (1 3)
            }
            
            s.pop()
            #s : [1]
        }
    s.pop()
    #s : []

    for문 i =1~3 i =2
    s : [2]
    ...
}
s : [1] -> [1,2] -> [1] -> [1,3] -> [1] 
           출력 -> pop(2)  출력 -> pop(3)
    
"""