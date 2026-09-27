'''
풀이 2: Counter로 줄인 풀이
- 흐름은 풀이 1과 같다(중복 제거 → 신고당한 횟수 → 메일 수)
- Counter는 없는 키를 조회하면 0을 돌려주므로 초기화가 필요 없다
- 시간 복잡도: O(신고 수 + 유저 수)
'''
from collections import Counter


def solution(id_list, report, k):
    report = set(report)                                  # 중복 신고 제거
    reportCount = Counter(r.split()[1] for r in report)   # 신고당한 횟수
    mail = Counter(r.split()[0] for r in report
                   if reportCount[r.split()[1]] >= k)     # 정지 대상을 신고한 사람별 메일 수
    return [mail[name] for name in id_list]
