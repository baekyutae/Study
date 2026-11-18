'''
1. 문제 파악

행의 갯수 row, 열의 갯수 col 
queries = [[x1,y1,x2,y2]]  리스트안 각좌표는 시계방향으로 한칸씩 회전하는 직사각형의 범위를 나타냄

각회전마다 위치가 바뀐 숫자들중 가장작은 숫자를 오름차순으로 배열에 담아 반환

주어진 정보를 활용해 특정한 답을 도출 -> 구현문제

----

x1~x2 범위의 행: 왼쪽 행 좌표는 -1, 우측 행 좌표는 +1
y1~y2 범위의 열: 위쪽 열 좌표는 +1, 아래쪽 열 좌표는 -1



2. 의사코드

def solution(rows, columns, queries):
    rows, columns로 2차원 maps 배열을 만듬
        배열은 0,0 부터 마지막 좌표 까지 1부터 rows*columns 가 순서대로 채워짐
        
    def clockSpin(x1,y1,x2,y2):
        좌표를 넣으면 시계방향으로 배열을 한칸씩 회전 시키고 최솟값을 반환
        좌측행 maps[(x1-1)~x2][y1]:
            이범위의 좌표에 숫자들은 모두 행이 -1 된 위치로 이동

        우측행 maps[x1~(x2-1)][y2]:
            이범위의 좌표에 숫자들은 모두 행이 +1 된 위치로 이동

        상단열 maps[x1][y1~(y2-1)]:
            이범위의 좌표에 숫자들은 모두 열이 +1 된 위치로 이동

        하단열 maps[x2][(y1+1)~y2]:
            이범위의 좌표에 숫자들은 모두 열이 -1 된 위치로 이동

            
        이동할때 매 좌표들을 temp = [] 에저장
        mini = min(temp)

        return mini

    answer = []
    quries에서 리스트를 하나씩 꺼냄
        minimum = clockSpint()
        answer.append(minimum)
    
    return answer

3. 엣지케이스
시간복잡도 최악의 케이스: 20만 200이라 괜찮음

4. 시간복잡도
시간복잡도
- 배열 생성: 2nm (n= rows, m = columns), maps를 만들고 또 칸을 채워넣었으니
- 회전: 테두리 길이 만큼 반복, 2(x2-x1)+2(y2-y1)-4 꼭짓점 4개는 행의 갯수 셀때 포함되니 4를 뺌
=> 2n+2m
- 쿼리의 갯수:k

매 쿼리마다 회전을 하니 k(n+m)
거기다 배열 생성 시간 nm

o(k(n+m)+nm)

공간복잡도
- maps : nm
'''

def solution(rows, columns, queries):
    # 2차원 배열 생성
    count = 1
    maps = [[0]*columns for _ in range(rows)] 
    for i in range(rows):
        for j in range(columns):
            maps[i][j] = count
            count += 1

    # 시계방향 회전 및 최소값 
    def clockSpin(x1,y1,x2,y2):
        # 좌표를 넣으면 시계방향으로 배열을 한칸씩 회전 시키고 최솟값을 반환
        # 좌측행 maps[(x1-1)~x2][y1]:
        #     이범위의 좌표에 숫자들은 모두 행이 -1 된 위치로 이동
        temp = maps[x1][y1]
        number = []
        for r in range((x1+1),x2+1):
            maps[r-1][y1] = maps[r][y1]        
            number.append(maps[r][y1])
        
        # 하단열 maps[x2][(y1+1)~y2]:
        #     이범위의 좌표에 숫자들은 모두 열이 -1 된 위치로 이동
        for c in range((y1+1),y2+1):
            maps[x2][c-1] = maps[x2][c]
            number.append(maps[x2][c])

        # 우측행 maps[x1~(x2-1)][y2]:
        #     이범위의 좌표에 숫자들은 모두 행이 +1 된 위치로 이동
        for r in range(x2-1,x1-1,-1):
            maps[r+1][y2] = maps[r][y2]
            number.append(maps[r][y2])
        # 상단열 maps[x1][y1~(y2-1)]:
        #     이범위의 좌표에 숫자들은 모두 열이 +1 된 위치로 이동
        for c in range(y2-1,y1,-1):
            maps[x1][c+1] = maps[x1][c]
            number.append(maps[x1][c])

        maps[x1][y1+1] = temp
        number.append(temp)

            
        # 이동할때 매 좌표들을 temp = [] 에저장
        mini = min(number)
        
        return mini

    answer = []
    # quries에서 리스트를 하나씩 꺼냄
    for x1,y1,x2,y2 in queries:
        minimum = clockSpin(x1-1,y1-1,x2-1,y2-1)
        answer.append(minimum)
    
    return answer
