"""
제한 시간 2초
N(4 ≤ N ≤ 20, N은 짝수)
1. 아이디어
팀 놔눠지는 경우의 수 따지기
20C10 : 3352,2128,6400
타임 아웃

"""
import sys
sys.stdin = open('./inputs/B_14889.txt','r')
N = int(sys.stdin.readline())
G = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

