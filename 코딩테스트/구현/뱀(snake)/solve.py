n = int(input())
k = int(input())
data = [[0]*(n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a,b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))

# 동, 남, 서, 북 => 시작이 오른쪽을 보고 있음
# index 0,1,2,3 방향 리스트를 시계방향으로 나열
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction,c):
    if c == "L": # 반시계방향, 파이썬은 음수도 % 하면 결과가 양수로 나옴
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4

    return direction

def snake_game():
    x,y = 1,1
    data[x][y] = 2 # 뱀이 있는 위치를 2로 
    direction = 0
    time = 0
    index = 0
    q = [(x,y)] # 뱅이 차지하는 좌표, 맨 앞 좌표가 꼬리
    while True:
        nx = x+ dx[direction]
        ny = y + dy[direction]
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
        else:
            time += 1
            break

        x,y = nx,ny
        time += 1
        if index < l and info[index][0] == time:
            direction = turn(direction,info[index][1])
            index += 1
    return time

print(snake_game())

