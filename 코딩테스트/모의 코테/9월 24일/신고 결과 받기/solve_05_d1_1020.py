'''
유저 리스트인  id_list , "신고한사람이름(공백)신고당한사람이름" 형태의 report, k 횟수 만큼 신고당하면 정지
정지를 당한 사람수 만큼 신고자가 메일을 받음

id_list 순서대로 각 유저가 받은 메일수를 반환

동일 유저에대한 중복 신고는 1회로 처리 -> repost를 중복 제거

알아야 하는 정보
1. 정지 대상자들
2. 정지 대상자들을 누가 신고했는지

reportMap = {신고당한사람 : [신고한사람 리스트]}

len(신고한사람 리스트) 가 k 이상이면 정지 대상
정지 대상 리스트 생성

정지 대상 리스트에 속한 key값의 value -> 메일 받을 사람들

------
시간복잡도
1. for r in setReport: -> setReport의 길이 유저수 n만큼 반복
2. for id in id_list, for getId in reportMap[id]: -> 최악의 경우 모든 유저가 서로를 신고했고 정지 대상이라면 n^2
3. mailNumber in mail.values(): -> n

o((n+n^2)

공간복잡도 
1. setReport 에 n
2. banList = set() 는 m
3. mail도 m
o(n+m)

edgecase
1. timeout error? : n의 최대값이 1000이므로 10만1000 -> 즉 걱정없음
2. 정지 대상자가 없다면?:  mail = {name:0 for name in id_list} 이고 banList에 들어 있어야 +=1 이므로 [0,0,0,0]같은 형태가 반환 
'''
def solution(id_list, report, k):
    # report에 중복 신고 제거
    setReport = set(report)

    reportMap = {name:[] for name in id_list}
    banList = set()

    for r in setReport:
        user, reportedUser = r.split(" ")
        reportMap[reportedUser].append(user)
        if len(reportMap[reportedUser]) >= k:
            banList.add(reportedUser)

    mail = {name:0 for name in id_list}
    # 메일 받을 사람 정리
    for id in id_list:
        if id in banList:
            # reportMap에서 신고한사람 리스트를 가져옴
            # 리스트를 보고 받을 메일수를 +=1 
            for getId in reportMap[id]:
                mail[getId] +=1
    answer = []
    for mailNumber in mail.values():
        answer.append(mailNumber)
    
    return answer
