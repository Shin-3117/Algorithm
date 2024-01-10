# 첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지를 출력한다.
A, B, C = map(int, input().split())

def dac(a,b,c):
    if b == 1:
        return a%c
    elif b%2 == 0:
        return (dac(a,b//2,c)**2)%c
    else:
        return ((dac(a,b//2,c)**2)*a)%c
    
sol = dac(A,B,C)
print(sol)