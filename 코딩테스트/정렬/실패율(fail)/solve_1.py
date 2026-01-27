'''
1단계 부터 n단계 까지 차례대로 실패율을 계산

단계 : 실패율 형태로 저장

매 단계 마다 해당 스테이지에 묶여 있는 사람들을 count로 체크해 전체 멤버수에서 제외

단계:실패율 딕셔너리를 실패율 기준으로 정렬

-------------------------

시간복잡도: NlogN

정렬하는데 NlogN
단계별로 실패율 계산 N*M : N개의 단계마다 count연산 (M개의 원소가 들은 리스트를 순회)

'''


def fail_rate(n: int, stages: list):
    cal_stages = stages 
    member = len(stages)
    fail = {}
    
    for i in range(1, n + 1):
        if member > 0:
            count = cal_stages.count(i)
            fail[i] = count / member
            member -= count 
        else:
            fail[i] = 0
    
    # fail[x] : lambda 식에서 sorted가 정렬 대상인 key들(x) 을 가져올 때 fail[x]에 전달 즉 vaule에 해당하는 값
    result = sorted(fail, key=lambda x: fail[x], reverse=True)
    return result
