import pytest
from solve import element_change

'''
정렬 했을때 a의 원소보다 b의 원소가 작아 교체 하지 않는 기능 체크
if a[i] < b[i]:
'''

cases =[
    ([110,100,50,60,12],
     [3,10,8,2,7],
     3,332)
]


@pytest.mark.parametrize("a,b,k,expected_result",cases)
def test_element_change(a,b,k,expected_result):
    assert element_change(a,b,k) == expected_result