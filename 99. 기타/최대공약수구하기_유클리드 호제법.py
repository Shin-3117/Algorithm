"""
유클리드 호제법
- 두 자연수 A,B 에 대하여 (A>B) A를 B로 나눈 나머지를 R일 때,
이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같습니다.
"""
def gcd(a, b):
    if a%b ==0:
        return b
    else:
        return gcd(b,a%b)