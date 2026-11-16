'''
디딤돌에 적힌 숫자가 담긴 배열 stones, 건너 뛸수 있는 최대 거리 k 가 주어짐

한명씩 개울을 건너며 가장 가까운 디딤돌을 통해 건너감, 지나갈때마다 디딤돌에 적힌 숫자가 1씩 줄어듬
0이된 디딤들은 밟지 못하며 건너 뛰어야 함
최대 거리 k를 초과해 건너뛰어야 하는 구간이 생기면 종료

건널수 있는 최대 인원을 반환

----

최대값 탐색, stones 원소의 최대값이 2억임 즉 한명씩 지나가는걸 추적하면 2억회 까지 연산이 될수 있음-> time out

지나가는 사람의 수를 매개변수로 두고 대입해 조건을 만족하면서 다 건너가 지는지를 탐색, 즉 dp로 해결

시간복잡도
1. while문 : log(max(stones)-min(stones))
2. for문 : stones의 길이 n
o(nlog(max(stones)-min(stones)))

공간복잡도
o(1)

edgecase
1. stones의 모든 원소가 1인 케이스 : 최대 1명 건널수 있음
2. 시간복잡도 최악의 케이스: 20만 * log 약2억 = 약 6백만 이하 문제 없음


'''

def solution(stones, k):
    # x명일 때 모두 지나가지는제 체크 함수
    def passCheck(x):
        p = 0
        for stone in stones:
            # stone이 x보다 크다면 x인원 다 그 돌 밟고 지나가니 문제 없음
            # stone이 x보다 작다면? 건너 뛰어야 할돌 +1
            # 건너 뛰어야 할돌 p가 k 이상만큼 누적되면? False 반환
            # 그전에 다시 x보다 작은 돌을 만나면? p는 0으로 초기화

            if stone >= x:
                p=0
            else:
                p+=1
                if p>=k: # 0인 디딤돌이 k개 이상 생기면 못건넘
                    return False

        return True

    # 탐색 범위 설정
    # k는 stones의 길이 이하 조건 때문에 최대 max(stones)까지만 지나갈수 있음: 그이후부턴 모든 돌이 0 이라 못지나감
    lo, hi = min(stones), max(stones)
    while lo<hi:
        mid = (lo+hi+1)//2 # lo와 hi가 1차이날때 올림을 안하면 lo=mid 에서 lo가 값변화 x --> 무한 순환
        if passCheck(mid):
            lo = mid
        else:
            hi = mid-1
    return lo
