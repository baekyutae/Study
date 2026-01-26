import pytest
from solve import element_change

'''
원소 교체가 제대로 이루어지는지 확인
sorted_a[i] = sorted_b[i]
'''
cases =[
    # 1. 일반예제
    ([1,2,5,4,3],
     [5,5,6,6,5],
     3, 26),

     # 2. k = n 전부  바꿔치기
    ([1,2,5,4,3],
     [5,5,6,6,5],
     5, 27),

    # 3. n,k 1이라면
     ([1],
     [1000],
     1, 1000)
     
]


@pytest.mark.parametrize("a,b,k,expected_result",cases)
def test_element_change(a,b,k,expected_result):
    assert element_change(a,b,k) == expected_result

# 결과 : 3 passed in 0.07s