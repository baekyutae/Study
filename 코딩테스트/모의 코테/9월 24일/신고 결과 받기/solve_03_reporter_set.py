'''
풀이 3: 신고당한 사람 → 신고한 사람 집합
- set에 넣는 순간 중복 신고가 저절로 1회로 처리된다(중복 제거를 따로 하지 않음)
- 신고한 사람 집합의 크기가 곧 신고당한 횟수다
- 시간 복잡도: O(신고 수 + 유저 수)
'''


def solution(id_list, report, k):
    reporters = {name: set() for name in id_list}  # 신고당한 사람 → 신고한 사람 집합
    for rp in report:
        reporter, reported = rp.split()
        reporters[reported].add(reporter)          # set이라 중복 신고가 저절로 1회로 처리됨

    mail = {name: 0 for name in id_list}
    for names in reporters.values():
        if len(names) >= k:                        # 신고한 사람 수 = 신고당한 횟수
            for name in names:
                mail[name] += 1
    return [mail[name] for name in id_list]
