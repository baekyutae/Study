import pytest
from solve_01 import fixed_point


cases = [
    # case 1 문제집 예제
    (5,[-15,-6,1,3,7],3),

    # case 2 n이 1 원소가 0
    (1,[0],0)

]

@pytest.mark.parametrize("n,num_list,expected_result",cases)
def test_fixed_point(n,num_list,expected_result):
    assert fixed_point(n,num_list) == expected_result
    

# 결과 2 passed in 0.05s 