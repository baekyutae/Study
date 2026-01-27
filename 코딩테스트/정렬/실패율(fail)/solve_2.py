'''
collection를 이용해 각 스테이지별 클리어를 하지 못한 인원 딕셔너리를 미리 만듬

stages = [2, 1, 2, 6, 2, 4, 3, 3]
counts = Counter(stages)

print(counts)
# 출력: Counter({2: 3, 3: 2, 1: 1, 6: 1, 4: 1})

해시 테이블을 만들어 딱 한번만 순회하므로 counter의 시간복잡도는 O(M)

전체 시간복잡도가 O(M + NlogN) 


때문에 count를 쓰는 solve_1 방식(M*N+NlogN)보다 M의 값 즉 게임 참여자의 수가 많을 수록 더 효율적이다.
'''



from collections import Counter

def solution(N, stages):
    # 1. 재고 목록(스테이지별 인원수)을 단 한 번에 만듭니다. O(M)
    counts = Counter(stages)
    
    total_players = len(stages)
    fail_rates = {}
    
    for i in range(1, N + 1):
        if total_players > 0:
            # 리스트를 다시 훑을 필요 없이 목록(counts)에서 바로 꺼냅니다. O(1)
            stuck_players = counts[i]
            fail_rates[i] = stuck_players / total_players
            total_players -= stuck_players
        else:
            fail_rates[i] = 0
            
    # 2. 정렬 O(N log N)
    return sorted(fail_rates, key=lambda x: fail_rates[x], reverse=True)