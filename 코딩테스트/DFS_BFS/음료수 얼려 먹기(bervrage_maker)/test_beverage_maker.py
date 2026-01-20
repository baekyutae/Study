import pytest
from solve import beverage_maker

cases=[

]



@pytest.mark.parametrize("n, m, graph, expected_Result",cases)
def test_beverage_maker(n,m,graph,expected_Result):
    assert beverage_maker(n,m,graph) == expected_Result