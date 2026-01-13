# n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def checker(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 기둥 인경우
            # '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False 

        elif stuff == 1: # 보 인경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False 
    return True

def builder(n, build_frame):
    answer = []
    for frame in build_frame: 
        x, y, stuff, operate = frame
        if operate == 0: # 삭제
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not checker(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치

        if operate == 1: # 설치
            answer.append([x, y, stuff]) # 일단 설치를 해본 뒤에
            if not checker(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거


    return sorted(answer) 

print(builder(n,build_frame))


'''
def builder(n, build_frame):
    make n*n wall
    build_frame의 원소(배열)를 하나씩 꺼냄

        기둥과 보를 설치 하는 경우
            answer에 더함
            checker()로 확인
            문제 없으면 유지 규칙 위반이면 remove

        기둥과 보를  삭제 하는 경우
            answer에서 remove 
            checker()로 확인
            문제 없으면 유지 규칙 위반이면 append

        
    
    return sort(answer)

def checker(answer):
    설치 및 삭제 했을때 조건에 위배 되지 않는지 체크
    설치/삭제가 기둥 일때 체크
        밑에 기둥이 있거나, 보의 끝에 위치

    설치/삭제가 기둥 일때 체크
        양쪽에 보가 연결되어 있거나 한쪽 끝 부분에 기둥이 있어야함

'''