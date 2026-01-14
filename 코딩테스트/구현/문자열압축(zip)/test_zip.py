import pytest
from solve import str_zip

cases = [
    # (s, expected_length)

    # 1) 일반예쩨
    ("aabbaccc", 7),          # "2a2ba3c"

    # 2) 전부 같은 문자
    ("aaaaaa", 2),            # "6a"

    # 3) 전부 다른 문자 (압축 이득 없음)
    ("abcdef", 6),

    # 4) 길이 1 (step 루프가 안 돌아도 정상)
    ("a", 1),

    # 5) 길이 2
    ("aa", 2),                # "2a"
    ("ab", 2),

    # 6) 반복 단위가 2에서 최적
    ("abababab", 3),          # step=2 -> "4ab"

    # 7) 반복 단위가 3에서 최적
    ("abcabcabc", 4),         # "3abc"

    # 8) 반복이 끊기고 꼬리가 남는 케이스
    ("abcabcdede", 8),        # step=3 -> "2abcdede" (길이 8)

    # 9) 숫자 자리수 증가(9->10) 확인
    ("aaaaaaaaaa", 3),        # "10a"

    # 10) 끝에 남는 조각(단위로 딱 안 나눠짐)
    ("aaaaa", 2),             # step=1 -> "5a"
    ("aaaaab", 3),            # "5ab" (또는 step=1이 최적)

    # 11) 부분 반복 + 다른 꼬리
    ("aabbaabb", 5),          # step=4 -> "2aabb"
]

@pytest.mark.parametrize("s,expected_result",cases)
def test_str_zip(s,expected_result):
    assert str_zip(s) == expected_result

# 결과: 13 passed in 0.06s