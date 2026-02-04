'''
top- down으로 푸는 방식

'''
import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 해제 

memo = [0] * 30001 

def make_one(x):
    if x == 1:
        return 0
    

    if memo[x] != 0:
        return memo[x]

    # -1 연산 (기본값 설정)
    res = make_one(x - 1) + 1

    # 각 연산을 비교하며 최솟값 갱신
    if x % 2 == 0:
        res = min(res, make_one(x // 2) + 1)
    if x % 3 == 0:
        res = min(res, make_one(x // 3) + 1)
    if x % 5 == 0:
        res = min(res, make_one(x // 5) + 1)


    memo[x] = res
    return res