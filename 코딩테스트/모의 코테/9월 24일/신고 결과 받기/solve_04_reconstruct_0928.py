'''
입력: 문자열 id_list, "신고한id 신고당한id" 형태의 문자열 배열 report

중복신고는 신고1회로 간주
k값 이상으로 신고당한 이용자는 정지 당하며 해당 유저를 신고한 이용자에게 메일이감

id_list 순서대로 받은 메일수를 반환, 받은적 없는 이용자는 0

----

일단 중복 신고는 1회로 간주 한다 했으니 report를 set 자료형으로 만들어 중복 제거

알아야하는 값은
1. 이용자별 신고당한 횟수를 기반으로 정지 리스트
2. 이용자별 신고한 사람 명단

id_list순으로 신고한 사람 명단이 정지리스트에 들어있을 때마다 받을 메일수 +=1


시간복잡도
1. idIdx 만들때 id_list의 길이 n
2.reportList  만들때 n
3. for ids in report: 중복이 제거된 report의 길이 m
3. # 받을 메일수 계산: 바깥 for문 n에 안쪽은 최악의 경우 n-1 -> n^2
o(n+m+n^2)

공간복잡도
(결과 반환용 answer 제외)
1. report: m
2. idIdx: n
3. bandList: n
4. reportList: n
5. reportCount = : n

o(n+m)

예외케이스
1. 시간 복잡도 최악의 케이스 : 10만 단위이므로 안전
2. ["a", "b"], ["a b", "b a"], 1 : 결과 [1,1] 확인
3. 정지 유저가 없는경우 ["a", "b"], ["a b", "b a"], 2 : [0,0]

'''

def solution(id_list, report, k):
    # 받을 메일 갯수 저장
    answer = [0]*len(id_list)
    report = set(report)
    idIdx = {name:idx for idx,name in enumerate(id_list)}
    banList = set()
    # 이용자별 신고한 사람 명단
    # reportList = {id:[신고id]}

    # 정지 횟수
    # reportCount = [idx순서별로]
    reportList = {name:[] for name in id_list}
    reportCount = [0]*len(id_list)
    # report에서 reporter와 reported를 꺼냄
    for ids in report:
        reporter, reported = ids.split(" ")
        reportList[reporter].append(reported)
        reportCount[idIdx[reported]] += 1
        if reportCount[idIdx[reported]] >=k:
            banList.add(reported)

    # 받을 메일수 계산
    for name, list in reportList.items():
        for id in list:
            if id in banList:
                answer[idIdx[name]] +=1

    return answer
