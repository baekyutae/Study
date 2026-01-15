import pytest
from solve import wall_check



cases = [
    # 1) 대표 예제
    (12, [1, 5, 6, 10], [1, 2, 3, 4], 2),
    (12, [1, 3, 4, 9, 10], [3, 5, 7], 1),

    # 2) 불가능한 케이스(-1): 취약점 대비 탐색거리와 수 부족
    (12, [1, 3, 4, 9, 10], [1, 1], -1),
    (30, [0, 3, 11, 21], [2], -1),

    # 3) 한바퀴 돌아 0을 넘어가는지
    (12, [0, 11], [1], 1),
    (12, [10, 11, 0, 1], [3], 1),

    # 4) 경계/단순
    (50, [10], [0], 1),
    (12, [1, 3, 4, 9, 10], [100], 1),

    # 5) dist 순서 섞여도 결과 동일
    (12, [1, 5, 6, 10], [4, 1, 3, 2], 2),

]


@pytest.mark.parametrize("n,weak,dist,expected_Result",cases)
def test_wall_check(n,weak,dist,expected_Result):
    assert wall_check(n,weak,dist) == expected_Result


# 결과: 9 passed in 0.06s