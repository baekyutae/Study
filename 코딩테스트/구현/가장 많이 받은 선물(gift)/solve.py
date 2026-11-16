def solution(friends, gifts):
    def giftIdx(p1, p2):
        # p1, p2의 선물 지수를 계산
        p1_idx = sum(giftMap[p1]) - sum(refundMap[p1])
        p2_idx = sum(giftMap[p2]) - sum(refundMap[p2])

        # 비교해서 누가 더 큰지를 반환
        if p1_idx > p2_idx:
            return p1
        elif p1_idx < p2_idx:
            return p2
        else:
            return 0

    # set {이름: idx} 0부터 시작
    # giftMap = {준사람1: [선물개수, 선물개수, ...], 준사람2: [...]}
    # refundMap = {받은사람1: [선물개수, 선물개수, ...], 받은사람2: [...]}
    # 딕셔너리의 value는 모두 friends의 idx 순으로 나열
    fIdx = {}

    for idx, name in enumerate(friends):
        fIdx[name] = idx

    giftMap = {
        name: [0] * len(friends)
        for name in friends
    }

    refundMap = {
        name: [0] * len(friends)
        for name in friends
    }

    for match in gifts:
        giver, receiver = match.split(" ")
        giftMap[giver][fIdx[receiver]] += 1
        refundMap[receiver][fIdx[giver]] += 1


    result = [0] * len(friends)

    # friends에 저장된 순으로 받아야 할 선물 수를 계산

    for idx1 in range(len(friends)):
        for idx2 in range(idx1+1, len(friends)):
            friend1 = friends[idx1]
            friend2 = friends[idx2]
            if friend2 == friend1:
                continue
            
            friend1Give = giftMap[friend1][fIdx[friend2]]
            friend2Give = giftMap[friend2][fIdx[friend1]]

            # 준 선물 수 비교
            if friend1Give > friend2Give:
                result[fIdx[friend1]] += 1

            elif friend1Give < friend2Give:
                result[fIdx[friend2]] += 1

            else:
                answer = giftIdx(friend1, friend2)

                if answer != 0:
                    result[fIdx[answer]] += 1


    return max(result)
