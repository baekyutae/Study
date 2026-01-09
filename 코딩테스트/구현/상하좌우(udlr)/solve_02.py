# 방향 벡터 리스트를 만들어 풀기

n = int(input())
plans = input().split()

def location_detector(n, plans):
    x, y = 1, 1

    
    # 순서: L, R, U, D
    dx = [0, 0, -1, 1] # 세로(행) 이동 변화량
    dy = [-1, 1, 0, 0] # 가로(열) 이동 변화량
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        # 이동 후 좌표 구하기
        nx, ny = 0, 0
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]
        
        # 공간을 벗어나는 경우 무시 (체크 후 이동 방식)
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
            
        # 이동 수행
        x, y = nx, ny

    return [x, y]

# 실행 및 출력
result = location_detector(n, plans)
print(result[0], result[1])