'''
이용자의 ID가 담긴 문자열 배열: id_list
이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열 report {"이용자id 신고한id"}
신고횟수 k

유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return

--------------
정보가 주어지고 정보를 필요한 형태로 가공해서 결과를 도출하는 함수를 만드는 문제 -> 구현

필요한 정보
1. 정지대상 목록: banList
2. banList에 있는 사람을 누가 신고했는지 -> 메일 받을 사람

일단 a가 b를 두번신고한건 하나로 친다 했으니 report에서 중복 제거


rinfo = {신고당한사람:[신고한사람]}

신고 당한사람이 banList에 있으면 rinfo[신고당한사람] -> 신고한 사람들에게 받을 메일 +=1

-----------
시간복잡도
1. idx 만드는 for문: id_list의 길이 n
2. for rp in setReport 의 길이 m
3. for reported, li in rinfo.items(): n -> 신고당한 사람수가 최대 n
거기다 k가 1이라 모든 사람이 정지 대상이라면
for id in li: n

=> n^2
o(n^2+m)

공간복잡도
1. setReport의 크기 m
2. rinfo: 신고당한사람수 n 에다가 각 value에 해당하는 리스트 n-1
-> 2n-1

3. banList: 최대 n

o(n+m)

풀이 26분, + 시간복잡도,공간복잡도 = 48분
'''
from collections import defaultdict

def solution(id_list, report, k):
    setReport = set(report)
    rinfo = defaultdict(list)
    banList = set()

    idx = {id:i for i,id in enumerate(id_list)}
    # setReport에서 banList와 rinfo 뽑아내기
    for rp in setReport:
        id, reported = rp.split(" ")

        # rinfo 만들기
        rinfo[reported].append(id)

        # 신고한 사람수가 k이상이면 banList에 추가
        if len(rinfo[reported])>=k:
            banList.add(reported)

    mail = [0]*len(id_list)
    # 받을 메일수를 계산
    # rinfo에서 reported, li를 꺼냄
    # reported가 bandList에 있으면
    # li를 순회하면서 받을 메일수를 +=1
    for reported, li in rinfo.items():
        if reported in banList:
            for id in li:
                mail[idx[id]] += 1

    return mail
