# 딕셔너리 활용

def location_detector_dict(n, plans):
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