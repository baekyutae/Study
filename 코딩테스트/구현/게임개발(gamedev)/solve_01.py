# 시간복잡도 O(N*M)

# 최악의 경우 모든 칸을 다 한번씩 방문

N, M = map(int, input().split())

x,y,dir = map(int, input().split())

game_map = []
check = []
for i in range(N):
    game_map.append(list(map(int, input().split())))
    check.append([0]*M)

check[x][y] = 1

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global dir
    dir -=1
    if dir == -1:
        dir = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x+dx[dir]
    ny = y+dy[dir]
    # 회전 이후 이동 가능
    if check[nx][ny] == 0 and game_map[nx][ny] == 0:
        check[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전 이후 이동 불가
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

print(f"가본 칸수 : {count}")


'''
북 동 남 서
dx = [-1,0,1,0] 
dy = [0,1,0,-1]

방위를 인덱스로 활용해 왼쪽으로 90도 회전한 후 한칸 이동한 좌표를 구함

ex) 0 : 북쪽을 바라보면 서쪽으로 회전후 한칸 이동 => x표는 그대로 y좌표는 -1 == dx[3], dy[3]

while 
    0. 방향회전, 회전한 방향으로 좌표 이동

    1. if : 이동한 좌표가 안가봤고 육지면 이동, count += 1, continue => 0으로 이동


    2. else: 바다거나 가본 장소면 turntime+=1, 3체크하고 1로


    3. turn_time = 4: 4방향다 가봤거나 바다면, 뒤로 한칸 이동, 뒤로 이동한 칸이 육지면 turn_time 초기화후 while문 시작으로
       바다면 while문 종료 후 가본 칸수 출력

'''