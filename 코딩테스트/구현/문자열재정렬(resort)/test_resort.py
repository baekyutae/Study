import pytest

def resort(give):
    str_list = []
    num_sum = 0
    
    for i in give:
        
        if i.isalpha():
            str_list.append(i)
        else:
            num_sum += int(i)
            
    
    str_list.sort()
    
    if num_sum != 0 or any(c.isdigit() for c in give):
        str_list.append(str(num_sum))
        
    return "".join(str_list)

cases = [
    #CASE 1 : 일반예제
    ("K1KA5CB7","ABCKK13"),

    #CASE 2: 전부 문자
    ("DCBAD", "ABCDD"),

    #CASE 3 : 전부 숫자
    ("4922134", "25")

]

@pytest.mark.parametrize("give, expected_result", cases)
def test_resort(give, expected_result):
    assert resort(give) == expected_result


# 결과 : 3 passed in 0.07s