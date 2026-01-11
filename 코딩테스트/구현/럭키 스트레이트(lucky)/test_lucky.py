import pytest

def skill_check(number):
    point = []
    for i in str(number):
        point.append(i)

    mid = len(point)//2

    left_sum = sum(int(i) for i in point[:mid])
    right_sum = sum(int(i) for i in point[mid:])

    if left_sum == right_sum:
        return("lucky")
    else:
        return("ready")


cases = [
    # case1 lucky가 나오는 경우
    (123402,"lucky"),

    #case2 ready가 나오는 경우
    (7755, "ready"),

    #case3 길이가 2인 정수
    (11,"lucky")

]

@pytest.mark.parametrize("number,expected_state",cases)
def test_skill_check(number,expected_state):
    assert skill_check(number) == expected_state

# 결과 : 3 passed in 0.05s