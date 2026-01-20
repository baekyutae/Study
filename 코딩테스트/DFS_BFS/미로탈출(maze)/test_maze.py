import pytest
from solve import maze
from copy import deepcopy

cases =[
    # 1. 일반예제
    (0, 0, 5, 6, [
        [1, 0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]
    ], 10),
    # 2. 외곽으로만 이동
    (0, 0, 5, 5, [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ], 9),
    # 3. 내려가다 다시 올라갔다 다시 내려가는 경로
    (0, 0, 5, 3, [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1]
    ], 11)
]

@pytest.mark.parametrize("x,y,n,m,graph,expected_result",cases)
def test_maze(x,y,n,m,graph,expected_result):
    #BFS 함수가 graph 내용을 수정하므로, 깊은 복사(deepcopy)를 해서 전달해야 
    # 테스트 케이스 원본이 오염되지 않음
    graph_copy = deepcopy(graph)
    assert maze(x,y,n,m,graph_copy) == expected_result


    # 결과 : 3 passed in 0.06s