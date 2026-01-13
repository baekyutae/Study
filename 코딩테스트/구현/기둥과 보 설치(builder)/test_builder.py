import pytest


def checker(answer):
    for x, y, stuff in answer:
        if stuff == 0: 
            
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False 
        elif stuff == 1: 
            
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False 
    return True

def builder(n, build_frame):
    answer = []
    for frame in build_frame: 
        x, y, stuff, operate = frame
        if operate == 0: 
            answer.remove([x, y, stuff]) 
            if not checker(answer): 
                answer.append([x, y, stuff]) 
        if operate == 1: 
            answer.append([x, y, stuff]) 
            if not checker(answer): 
                answer.remove([x, y, stuff]) 


    return sorted(answer) # 정렬된 결과를 반환

cases = [
    # case 1 일반예제
    (
        5,
        [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]],
        [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]
    ),
    # case 2 만들었다가 전부 삭제 (최종 결과는 빈 배열)
    (
        5,
        [
            [0,0,0,1],  # 기둥 설치(바닥)
            [2,0,0,1],  # 기둥 설치(바닥)
            [4,0,0,1],  # 기둥 설치(바닥)
            [2,0,0,0],  # 기둥 삭제
            [0,0,0,0],  # 기둥 삭제
            [4,0,0,0],  # 기둥 삭제
        ],
        []
    ),

    # case 3 설치/삭제 조건 위배 (위배되는 작업은 무시되거나 롤백되어 최종 구조 유지)
    (
        5,
        [
            [1,1,1,1],  # (위배) 보 설치 시도: 지지 없음 -> 무시되어야 함
            [1,0,0,1],  # 기둥 설치(바닥) -> OK
            [1,1,1,1],  # 보 설치: (1,0) 기둥이 지지 -> OK
            [2,1,0,1],  # 기둥 설치: (1,1) 보가 (x-1,y)로 지지 -> OK
            [1,1,1,0],  # (위배) 보 삭제 시도: (2,1) 기둥이 붕 뜸 -> 롤백되어야 함
            [1,0,0,0],  # (위배) 기둥 삭제 시도: 보가 지지 잃음 -> 롤백되어야 함
        ],
        [[1,0,0],[1,1,1],[2,1,0]]
    ),
]

@pytest.mark.parametrize("n, build_frame, expected_result", cases)
def test_builder(n, build_frame, expected_result):
    assert builder(n, build_frame) == expected_result

# 결과:  passed in 0.05s