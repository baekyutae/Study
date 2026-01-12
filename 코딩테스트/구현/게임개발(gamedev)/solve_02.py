# 재귀 함수 형태

import sys
# 파이썬 자체적으로 재귀함수가 1000번 이상 호출하면 중단시키는데 이 제한을 늘림
sys.setrecursionlimit(10**6)

# 1. 로직 (Function)
def solve_recursive(N, M, x, y, dir, game_map, count=1):
    game_map[x][y] = 2 # 방문 처리 (외부에서 넘겨받은 game_map을 직접 수정) : 0은 육지 1은 바다 2는 방문
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    # 이동 가능한 방향 탐색
    for i in range(1, 5):
        nd = (dir - i + 4) % 4 
        nx, ny = x + dx[nd], y + dy[nd]
        
        if game_map[nx][ny] == 0:
            return solve_recursive(N, M, nx, ny, nd, game_map, count + 1)

    # 이동을 더 이상할수 없으면 후진 시도
    #      
    back_x, back_y = x - dx[dir], y - dy[dir]

    # 뒤쪽이 바다(1)가 아니라면 (육지 0 이거나 이미 간 곳 2) 후진
    if game_map[back_x][back_y] != 1: 
        return solve_recursive(N, M, back_x, back_y, dir, game_map, count)
    
    # 이동도 안되고 후진도 안되면 결과 반환
    return count


# 2. 실행 코드 (Main)
if __name__ == "__main__":
    # (1) 여기서 game_map을 만듭니다.
    N, M = map(int, input().split())
    x, y, dir = map(int, input().split())
    
    game_map = []
    for _ in range(N):
        game_map.append(list(map(int, input().split())))

    # (2) 만들어진 맵을 함수에 전달
    result = solve_recursive(N, M, x, y, dir, game_map)
    
    # (3) 결과 출력
    print(result)