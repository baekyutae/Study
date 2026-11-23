'''
1. 문제 분석
행, 열의 갯수가 rows, columns 로 주어짐 
queries로 회전하는 태두리의 좌상단 우하단 좌표가 [[x1,y1,x2,y2],[...]]로 주어짐
매 [...] 마다 시계방향으로 한칸씩 이차원 배열의 원소들이 회전할때
회전에 의해 위치가 바뀐 숫자중 가장 작은 숫자들을 순서대로 배열에 담아 return 

처음 행렬은 가로 방향으로 1부터 숫자가 1씩 증가하며 적혀있음

2. 의사코드
def solution(rows, columns, queries):

    1부터 1씩 가로로 증가하며 적힌 2차원 배열 maps를 생성

    회전을 한뒤 최솟값을 반환하는 함수
    def spin(x1,y1,x2,y2):
        좌표를 넣으면 maps에서 회전
            temp = x1,y1 -> 한칸을 일단 빼둬서 회전가능하게 함
            좌측 테두리를 위쪽부터 위로 한칸씩 이동(덮어씌움) / x1,y1 제외
            아래쪽 테두리를 왼쪽부터 왼쪽으로 이동
            오른쪽 테두리를 아래쪽 부터 밑으로 한칸씩 이동
            위쪽 테두리를 오른쪽 부터 오른쪽으로 한칸씩 이동 / x1,y1 제외

            temp를 오른쪽으로 한칸 이동

        
        이동하면서 원소들을 모두 con = []에 저장
        return min(con)

    queries에서 좌표가 들어있는 []를 꺼내
    minNumber= spin()에 넣음
    answer = []

    answer.append(minNumber)
    return answer

'''
def solution(rows, columns, queries):
    maps = [[0]*columns for _ in range(rows)]
    count = 1
    for i in range(rows):
        for j in range(columns):
            maps[i][j] = count
            count +=1

    def spin(x1,y1,x2,y2):
        temp = x1,y1
        con = []
        # 좌측 테두리
        for r in range(x1+1,x2+1):
            maps[r-1][y1] = maps[r][y1]
            con.append(maps[r][y1])
        # 하단 테두리
        for c in range(y1+1,y2+1):
            maps[x2][c-1] = maps[x2][c]
            con.append(maps[x2][c])
        # 우측 테두리
        for r in range(x2-1,x1-1,-1):
            maps[r+1][y2] = maps[r][y2]
            con.append(maps[r][y2])
        # 상단 테두리
        for c in range(y1+1,y2):
            maps[x1][c+1] = maps[x1][c]
            con.append(maps[x1][c])

        r,c = temp
        maps[x1][y1+1] = maps[r][c]
        con.append(maps[r][c])
        return min(con) 

    answer = []
    for x1,y1,x2,y2 in queries:
        minNum = spin(x1-1,y1-1,x2-1,y2-1)
        answer.append(minNum)
    return answer

queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
rows = 6
columns = 6

solution(rows,columns,queries)