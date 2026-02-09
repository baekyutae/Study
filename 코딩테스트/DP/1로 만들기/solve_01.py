'''
bottom-up 으로 푸는 방식

1은 구하려는 최종값이니 필요 연산횟수가 0

dp테이블을 생성
정수 2부터 x까지 만들기 위한 최소 연산을 dp 테이블에 저장

어떤 수든 1 빼기는 가능하니 기준으로 설정
이후 2,3,5로 나누어지는 경우 1까지 구하는 연산 횟수를 비교하여 최솟값을 dp 테이블에 저장

'''

def make_one(x):
    table =[0] * 30001
    for i in range(2, x+1):
        # -1 연산 :  i-1을 1로 만들기 위한 위한 최소 연산 횟수 + -1 연산을 실행 (연산 횟수 +1)
        table[i] = table[i-1] + 1

        if i % 2 == 0:
            # table[i] : -1 연산 했을 떄의 최소연산과, 2로 나누는 연산(+1) + 숫자 i//2를 구하는 최소 연산 횟수 을 비교
            table[i] = min(table[i], table[i//2]+1)

        if i % 3 == 0:
            table[i] = min(table[i], table[i//3]+1)

        if i % 5 == 0:
            table[i] = min(table[i], table[i//5]+1)

    return table[x]