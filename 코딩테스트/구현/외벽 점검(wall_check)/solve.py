from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수: 1부터 시작

            # 해당 친구가 점검할 수 있는 마지막 위치
            # 취약점에서 시작 + 1시간에 이동 가능한 거리
            position = weak[start] + friends[count - 1]
            
            # 시작점부터 모든 취약한 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer


'''
itertools.permutations 용도

from itertools import permutations

permutations(iterable, r=None)

iterable: 순열을 만들 대상 (리스트/튜플/문자열 등)

순열: 순서까지 고려한 조합 => (1,2) 와 (2,1)이 다르게 취급
r: 뽑을 길이(개수)

생략하거나 None이면 r = len(iterable) (전부 뽑는 순열)

반환값은 이터레이터이고, 각 원소는 튜플로 나옴

ex)
list(permutations([1, 2, 3], 2))
# 결과:  [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

'''