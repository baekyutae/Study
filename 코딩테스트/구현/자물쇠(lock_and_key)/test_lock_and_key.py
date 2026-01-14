import pytest
from solve import lock_and_key


cases = [
    # (key, lock, expected)

    #1) 일반 예제 (회전/이동 필요)
    (
        [[0,0,0],
         [1,0,0],
         [0,1,1]],
        [[1,1,1],
         [1,1,0],
         [1,0,1]],
        True
    ),

    # 2) 이미 lock이 전부 1인데 key가 0만 있음 -> 항상 True (어디 놓든 중앙은 1 유지)
    (
        [[0]],
        [[1]],
        True
    ),

    # 3) lock에 홈(0)이 있는데 key가 모두 0 -> 절대 못 채움
    (
        [[0,0],
         [0,0]],
        [[1,0],
         [1,1]],
        False
    ),

    # 4) 홈 1개를 1개 돌기로 정확히 메우는 가장 단순 케이스
    (
        [[1]],
        [[0]],
        True
    ),



    # 5) 경계에서만 맞는 케이스(확장 3배 로직 검증용)
    #    lock의 (0,0)이 홈이고, key의 돌기가 한 칸만 있어서 모서리에 맞춰야 함
    (
        [[1,0],
         [0,0]],
        [[0,1],
         [1,1]],
        True
    ),

    # 6) 회전이 있어야만 열리는 케이스(rotate 로직 검증)
    (
        [[1,0],
         [1,0]],
        [[1,1],
         [0,1]],
        True
    ),

    # 7) 홈이 여러 개인데 key 돌기 수가 부족 -> False
    (
        [[1,0],
         [0,0]],
        [[0,0],
         [1,0]],
        False
    )

]

@pytest.mark.parametrize("key,lock,expected_result",cases)
def test_lock_and_key(key,lock,expected_result):
    assert lock_and_key(key,lock) == expected_result


# 결과: 7 passed in 0.06s