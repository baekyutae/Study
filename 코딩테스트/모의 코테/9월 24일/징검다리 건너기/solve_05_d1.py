'''
한사람씩 징검다리를 건넘
건널때마다 밟는 돌에 적힌 숫자가  1씩 줄어듬
0이된 돌은 밟을수 없고 건너뛰어야함
건너뛸수 있는 최대 칸수는 k

숫자가 적힌 돌의 배열은 stones

최대 몇명까지 건널수 있는지 반환하는 함수를 만들어라

일단 돌에 적힌 숫자 최대값이 2억이므로 한명씩 지나가는 연산으론 time out 
규칙을 일일히 구현하기 보다 건너는 사람수를 매개변수로 잡고 모두 건너지는지 체크해 결과에 따른 이분탐색 실행 -> 파라매트릭 서치



'''
def solution(stones, k):
    def check(people: int):
        # 사람수 people이 모두 건너지는지 여부 t/f 반환
        # stones를 하나씩 탐색
        # stones[i] > people 이라면 건너뛰어 넘는 순간이 옴
        # 건너뛰어야 하는 돌 jump +=1
        # stones[i+1] > people이면 누적
            # jump >= k 가 되면 false 반환
        # 그전에 stones[j] <= people을 만나면 jump 초기화
        jump = 0
        for number in range(len(stones)):
            if stones[number] < people:
                jump += 1
                if jump >= k:
                    return False
            else:
                jump = 0

        return True

    # 이진 탐색 로직
    lo, hi = 1, max(stones)
    while lo<hi:
        mid = (lo+hi+1)//2 # lo랑 hi가 1차이나는경우 고려 1 올림
        if check(mid):
            lo = mid
        else:
            hi = mid-1
    
    return lo

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
solution(stones,k)