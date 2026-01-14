import pytest

from solve import snake_game


cases = [
    # case 1 : 일반예제
    (
        6,
        [(3, 4), (2, 5), (5, 3)],
        [(3, "D"), (15, "L"), (17, "D")],
        9,
    ),
    # case2 사과 없음, 방향전환 없음: 오른쪽으로 가다가 벽에 충돌
    (
        3,
        [],
        [],
        3,  # (1,1)에서 (1,2)(1,3) 후 다음에 (1,4) 시도 -> 3초에 종료
    )

]


@pytest.mark.parametrize("n, apples, moves, expected", cases)
def test_snake_game(n, apples, moves, expected):
    assert snake_game(n, apples, moves) == expected

# 결과: 2 passed in 0.06s 