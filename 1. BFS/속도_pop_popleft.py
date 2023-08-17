from collections import deque
import time

for i in range(5,9):
    a_var = deque([x for x in range(10**i)])
    cur_time0 = time.time()
    a_var.popleft()
    print(f'popleft 10^{i} :',time.time()-cur_time0)

    d_var = [x for x in range(10**i)]
    cur_time3 = time.time()
    d_var.pop(0)
    print(f'pop(0) 10^{i} :',time.time()-cur_time3)
    print('-----------')
"""
popleft 10^5 : 0.0
pop(0) 10^5 0.0
-----------
popleft 10^6 : 0.0
pop(0) 10^6 0.0010704994201660156
-----------
popleft 10^7 : 0.0
pop(0) 10^7 0.015621185302734375
-----------
popleft 10^8 : 0.0
pop(0) 10^8 0.062488555908203125
-----------
"""
"""
10^9 부터는 시간이 너무 걸림(시간초과)
실험 결과 10^5(10만) 까지는 pop(0)도 괜찮은 선택지로 보임
"""