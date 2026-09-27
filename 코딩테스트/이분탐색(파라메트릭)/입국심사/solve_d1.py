def solution(n, times):
    # 후보 시간 t 안에 처리 가능한 총 인원수를 센다
    def passCheck(t):
        result = sum(t // time for time in times)
        return result

    # 최소시간은 항상 lo와 hi 사이에 존재한다
    lo, hi = 1, min(times) * n
    while lo < hi:
        mid = (lo + hi) // 2
        if passCheck(mid) >= n:
            hi = mid
        else:
            lo = mid + 1

    return lo
