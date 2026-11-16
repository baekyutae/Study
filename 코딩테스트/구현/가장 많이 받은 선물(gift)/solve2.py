def solution(friends, gifts):
    n = len(friends)
    idx = {name: i for i, name in enumerate(friends)}
    count = [[0] * n for _ in range(n)]
    gift_index = [0] * n
    for g in gifts:
        a, b = g.split()
        count[idx[a]][idx[b]] += 1
        gift_index[idx[a]] += 1   # 선물지수를 입력 읽을 때 미리 계산
        gift_index[idx[b]] -= 1
    receive = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if count[i][j] > count[j][i]:
                receive[i] += 1
            elif count[i][j] < count[j][i]:
                receive[j] += 1
            elif gift_index[i] > gift_index[j]:
                receive[i] += 1
            elif gift_index[i] < gift_index[j]:
                receive[j] += 1
    return max(receive)
