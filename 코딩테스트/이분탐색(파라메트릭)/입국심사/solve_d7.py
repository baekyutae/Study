'''
심사받아야할 사람 n명, 심사걸리는 시간 배열 times
n명이 심사 다받는데 걸리는 시간의 최솟값을 return

시간을 파라미터로 했을때 N명이 심사 가능한지 y/n으로 판별 가능
최대 10억명이 심사를 받아야함, 한명씩 심사관에 배정하는 로직으론 Timeout

-> 파라매트릭 서치

시간복잡도
1. while 문 log(min(times)*n)
2. canPass(t) : times의 길이 m
o(mlog(min(times)*n))

공간복잡도
o(1)

edgecase
1. 시간복잡도 최악: 10만 * log 10억^2 -> 6백만 (10억^2은 대기 인원 최대값 * 심사관이 처리하는데 걸린 시간 최소값이 10억)

'''

def solution(n, times):
    def canPass(t): # 시간이 t일때 n명을 심사 다 봐줄수 있는지 여부
        result = 0 # 몇명 처리할수 있는지 결과

        for time in times: # 각 심사관이 쳐내는 인원순
            result += t//time

        if result >= n:
            return True
        else:
            return False

    lo, hi = 1, min(times)*n # 최소 한시간은 필요하고, 최대 제일 적게 걸리는 검사관이 전부 다봐주는 경우
    while lo<hi:
        mid = (lo+hi)//2
        if canPass(mid):
            hi = mid
        else:
            lo = mid+1
    return lo
