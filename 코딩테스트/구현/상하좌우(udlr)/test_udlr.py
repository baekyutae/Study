import pytest

def location_detector(n, plans):
    x, y = 1, 1
    # 방향을 키(Key)로, 이동량을 값(Value)으로 매핑
    moves = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0)
    }

    for plan in plans:
        # 딕셔너리에서 바로 값을 꺼냄 (O(1)) -> if문/for문 없음
        dx, dy = moves[plan]
        
        nx, ny = x + dx, y + dy
        
        if 1 <= nx <= n and 1 <= ny <= n:
            x, y = nx, ny
            
    return [x, y]


# 테스트 코드

test_cases = [
    # CASE 1: U 방향으로 초과
    (5, ['R', 'R', 'R', 'U', 'D', 'D'], [3, 4]),

    # CASE 2: 벽 긁기 (R, D, L 순서대로 끝까지 이동 시도)
    (5, ['R']*5 + ['D']*5 + ['L']*5, [5, 1]),

    # CASE 3: 최소 단위 이동(한번 이동)
    (5, ['R'], [1, 2]),

    # CASE 4: 시작하자마자 벽으로 이동 (이동 불가 확인)
    (5, ['L', 'L', 'U', 'U'], [1, 1]),

    # CASE 5: N=1 (1x1 맵에서는 움직일 수 없음)
    (1, ['R', 'U', 'D', 'L'], [1, 1]),
    
    # CASE 6: 제자리 왕복 (갔다가 되돌아오기)
    (5, ['R', 'L', 'D', 'U'], [1, 1]),
]

@pytest.mark.parametrize("n, plans, expected", test_cases)
def test_location_detector(n, plans, expected):
    """
    딕셔너리 기반 location_detector 함수가
    모든 엣지 케이스를 통과하는지 검증
    """
    assert location_detector(n, plans) == expected

# 실행결과
# 6 passed in 0.05s