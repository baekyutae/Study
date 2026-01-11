import pytest

# game.py

def game_dev(N, M, x, y, dir, game_map):
  
    check = [[0] * M for _ in range(N)]
    check[x][y] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 내부 함수에서 상위 변수(dir)를 수정하기 위해 nonlocal 사용
    # global 쓰면 game_dev함수 바깥에서 찾으려 함
    def turn_left():
        nonlocal dir
        dir -= 1
        if dir == -1:
            dir = 3

    count = 1
    turn_time = 0

    while True:
        turn_left()
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if check[nx][ny] == 0 and game_map[nx][ny] == 0:
            check[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue
 
        else:
            turn_time += 1

        if turn_time == 4:
            nx = x - dx[dir]
            ny = y - dy[dir]

            if game_map[nx][ny] == 0:
                x = nx
                y = ny
            else:
                break
            turn_time = 0
            
    return count

cases = [
    # CASE 1: 일반적인 4x4 예시 (책 예제)
    (
        4, 4, 1, 1, 0,
        [
            [1, 1, 1, 1],
            [1, 0, 0, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1]
        ], 
        3
    ),

    # CASE 2: 고립된 섬 (시작 지점 주변이 모두 바다)
    (
        3, 3, 1, 1, 0,
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ], 
        1
    ),

    # CASE 3: 막다른 길에서 후진 후 종료
    # (1,1) -> (2,1)로 이동 후 막혀서 다시 (1,1)로 후진, 뒤도 바다라 종료
    (
        4, 3, 1, 1, 0,
        [
            [1, 1, 1],
            [1, 0, 1],
            [1, 0, 1],
            [1, 1, 1]
        ], 
        2
    ),

    # CASE 4: 일직선 이동 
    (
        3, 5, 1, 1, 1,
        [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ], 
        3
    ),
]

@pytest.mark.parametrize("N, M, x, y, dir, game_map, expected_count", cases)
def test_game_dev(N, M, x, y, dir, game_map, expected_count):
    assert game_dev(N, M, x, y, dir, game_map) == expected_count

# 결과: 4 passed in 0.04s