'''
1.문제 파악

디딤돌에 숫자가 있고 밟을 때마다 -1, 0 이되면 건너 뛰어야 함
한번에 한명씩 건너며 건너뛸수 있는 칸수 k가 제한됨

돌에 적히는 숫자는 최대 2억, 건너는 사람의 수는 제한 없음 즉 최대 2억명까지 지나가는데, 이걸 매번 지나가는 로직을 돌린다? -> time out

사람수를 파라미터로 잡고 최소 최대 범위안에서 이진 탐색 - > 파라매트릭 서치
lo,hi,mid 다 지나가지면 lo = mid , 다 못지나가면 hi = mid-1

2. 엣지케이스
k보다 건너뛰어넘어야 하는 돌이 더 많은 경우: count로 누적을 해서 k와 동일해지면 False를 반환, k와 동일해지기 전에 연속이 끊기면 다시 0으로 초기화
차피 매번 canCross로 검사하므로 p가 늘게되어 k보다 count가 이상이 되더라도 다 잡아냄

3. 시간/공간복잡도
시간복잡도
- 이진탐색: log(max(stones)-1)
- canCross: 매번 stones길이 n만큼 for문 돌림

nlog(max(stones)-1)

공간복잡도
o(1)

'''

def solution(stones, k):
    # 사람 숫자 p를 넣으면 p명이 다 징검다리를 건널수 있는지 체크
    def canCross(p):
        # stones에 각 돌에다가 p를 빼본다.
        # 0보다 작으면 그돌은 건너뛰어야 하는 순간이온단 뜻
        # 건너뛰어야하는 돌(p보다 작은)이 연속으로 k개가 되면 못건넌다 판단
        # 
        count = 0 
        for i in stones:
            if i<p:
                count +=1
                if count == k:
                    return False
            else:
                count = 0
        return True

    # 돌에 적힌숫자 최솟값은 1 이니 최소 한명은 지나갈수 있어야 하고, stones에 적힌 최대값 만큼 건너갈수 있음
    # 왜? : k는 stones길이 이하 즉 stones에 돌이 모두 0 이되었을때 한번에 개울을 뛰어넘지는 못함
    lo,hi = 1, max(stones)
    while lo<hi:
        mid = (lo+hi+1)//2 # lo와 hi가 1차이나면 lo=mid일때 lo가 변화 없이 그대로이므로 올림 해준다.

        # 다 건너지면 증가
        if canCross(mid):
            lo = mid
        else:
            hi = mid-1

    return lo