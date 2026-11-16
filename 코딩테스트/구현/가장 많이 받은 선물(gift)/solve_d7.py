'''
1. a와 b 상호간에 선물을 더 많이 준쪽이 다음달에 선물을 받음
2. 선물을 주고받은적이 없거나 같다면, 선물지수를 비교해 더큰사람이 하나 받음
    선물지수: 준선물 - 받은선물
3. 선물지수도 같다면 둘다 선물을 안받음

가장 선물을 많이 받는 친구의 받는 선물수를 반환

이름을 담은 문자열 배열 friends, ["선물준사람A 받은사람B"] 형태의 배열 gifts
A와 B가 같은 이름인 경우는 존재하지 않음


세로축을 준사람, 가로축을 받은사람, 순서는 friends 이름순으로 원소는 준 선물개수를 나타낸 2차원 배열을 만든다면?
각 이름에 대응되는 인덱스를 딕셔너리로 만듬 - > 인덱스 값으로 2차원 배열에서 a와 b를 찾아 선물을 주고받은 갯수를 비교

선물지수 gIdx 도 friends 순으로 저장
default 0으로 두고 gifts에서 하나씩 꺼낼때마다 +1 -1로 갱신

------------

시간복잡도
1. 인덱스 생성: friends의 길이 n
2. 2차원 배열 생성: n^2
3. gMap 값 채워 넣기: gifts의 길이 m
4. 마지막 이중 for문: n^2

o(n^2+n+m)

공간복잡도
1. gIdx: n
2. findex: n
3. gMap: n^2
4. result: n
o(n^2+n)
'''

def solution(friends, gifts):
    gIdx = [0]*len(friends)
    findex = {}
    # 이름과 인덱스를 대응
    for idx, name in enumerate(friends):
        findex[name] = idx
    # 주고 받은 선물수를 나타낸 2차원 배열 생성
    gMap = [[0]*len(friends) for _ in range(len(friends))]

    # gifts를 사용 gMap을 채워넣기
    for c in gifts:
        giver, taker = c.split(" ")
        gMap[findex[giver]][findex[taker]] += 1
        # 선물 인덱스도 갱신: 준 사람은 +=1, 받은사람은 -=1
        gIdx[findex[giver]] +=1
        gIdx[findex[taker]] -=1

    result = [0]*len(friends)
    #  이제 friends 간 주고받은 선물수와 선물지수를 확인해 받을 선물수를 저장
    for i in range(len(friends)):
        for j in range(i,len(friends)):
            if i != j:
                # friends[i]가 선물을 더 많이 줬다면
                if gMap[i][j] > gMap[j][i]:
                    result[i] +=1
                # friends[j]가 선물을 더 많이 줬다면
                elif gMap[i][j] < gMap[j][i]:
                    result[j] += 1
                # 선물지수 비교
                elif gIdx[i] > gIdx[j]:
                    result[i] += 1
                elif gIdx[i] < gIdx[j]:
                    result[j] += 1
                else:
                    continue

    return max(result)
