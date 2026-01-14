
'''
1. 열쇠의 이동을 위한 자물쇠 사이즈*3

2. 90도 회전 함수

'''


def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행의 길이
    m = len(a[0]) # 열의 길이

    # 90도 회전한 2차원 배열 틀 짜기
    result = [[0]*n for _ in range(m)]

    # 90도 회전한 좌표로 이동
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]

    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock)//3 # 3배로 늘린 자물쇠 배열에서 실제 자물쇠가 시작되는 지점
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
            
    return True


def lock_and_key(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    #  확장된 자물쇠 배열에 실제 자물쇠 배열의 홈과 돌기 반영   
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        # n*2 : 확장된 자물쇠 범위내에서 움직이기 위함 
        # 자물쇠 행열의 길이가 각각 3이고 9로 3배 확장되었으면: 0~2, 3~5, 6~8 즉 자물쇠의 시작 인덱스가 6까지 가능

        # x,y는 new_lock에서 열쇠배열이 놓일 위치를 지정(열쇠배열 좌측상단 좌표)
        # 기존 new_lock 좌표에 열쇠배열의 값들을 더해 check함수에서 열쇠가 자물쇠의 홈을 모두 메우는지 확인(전부 1, 0이나 2가 있음 False)
        for x in range(n*2):
            for y in range(n*2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                if check(new_lock) == True:
                    return True
                # 자물쇠를 열지 못하면 더했던 값을 다시 지워 new_lock이 처음 만들어졌던 상태로 복구, 다시 x,y 좌표 for문으로 복귀해 열쇠 위치를 이동
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False
