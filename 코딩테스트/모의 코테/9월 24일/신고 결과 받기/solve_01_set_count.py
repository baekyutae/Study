'''
풀이 1: 입력 중복 제거 + 다 센 뒤 정지 판정
- set(report)로 같은 사람을 여러 번 신고한 기록을 1회로 만든다
- 신고당한 횟수를 전부 센 뒤에 정지 대상을 한 번에 판정한다
- 시간 복잡도: O(신고 수 + 유저 수)
'''


def solution(id_list, report, k):
    report = set(report)  # 같은 사람을 여러 번 신고해도 1회로 처리

    # 1. 사람별로 신고당한 횟수를 센다
    reportCount = {name: 0 for name in id_list}
    for rp in report:
        _, reported = rp.split()
        reportCount[reported] += 1

    # 2. 다 센 뒤에 정지 대상을 한 번에 판정한다
    banList = {name for name, cnt in reportCount.items() if cnt >= k}

    # 3. 정지 대상을 신고한 사람에게 메일 1통씩
    mail = {name: 0 for name in id_list}
    for rp in report:
        reporter, reported = rp.split()
        if reported in banList:
            mail[reporter] += 1

    return [mail[name] for name in id_list]
