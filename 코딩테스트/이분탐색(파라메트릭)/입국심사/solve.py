def solution(n, times):
    # 매개변수인 시간 t가 주어졌을때 처리 가능 인원과 n을 비교
    def check(t):
        return sum(t//time for time in times) >= n 
    
    lo,hi = 1,min(times)*n
    while lo<hi:
        mid = (lo+hi)//2
        
        if check(mid):
            hi = mid
        else:
            lo = mid+1
            
            
    return lo
