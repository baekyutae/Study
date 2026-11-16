def solution(friends, gifts):
    # fIdx
    fIdx = {}
    for i, friend in enumerate(friends):
        fIdx[friend] = i
    
    giftIdx = [0]*len(friends)
    # 주고 받은 선물수를 2차원 배열로 저장
    giftMap = [[0]*len(friends) for _ in range(len(friends))]
    for match in gifts:
        giver, get = match.split(" ")
        giftMap[fIdx[giver]][fIdx[get]] +=1
        giftIdx[fIdx[giver]]+=1
        giftIdx[fIdx[get]]-=1
    
    result = [0]*len(friends)
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if giftMap[i][j] > giftMap[j][i]:
                result[i] +=1
                
            elif giftMap[i][j] < giftMap[j][i]:
                result[j] +=1
                
            elif giftIdx[i] >giftIdx[j]:
                result[i] +=1
            
            elif giftIdx[i] < giftIdx[j]:
                result[j] +=1
                
            else:
                continue
            
    return max(result)
