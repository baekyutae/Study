from solve import ant_worrior
import pytest


cases =[
    ([1,3,1,5],4,8),

]

@pytest.mark.parametrize("ware_house, n, expected_result", cases)
def test_ant_worrior(ware_house, n, expected_result):
    assert ant_worrior(ware_house, n) == expected_result