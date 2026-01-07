# O(N+M)

n, m = map(int, input().split())

Ball_weight = map(int, input().split())



def Select_Ball(n,m,Ball_weight):
    # 무게 별 공 개수
    array = [0] * (m+1)
    
    for x in Ball_weight:
        array[x] += 1
    # print(array)
    result = 0
    for i in range(1, m+1):
        n -= array[i] # 들고있는 무게의 공 갯수 제외
        result += array[i] * n

    print(result)


Select_Ball(n,m,Ball_weight)