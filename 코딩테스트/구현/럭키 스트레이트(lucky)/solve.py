# 시간복잡도는 O(n) 
#  자릿수의 길이만큼 for문 돌아감 => n
# 반으로 나눠서 sum  = > n/2 + n/2 == n


number = int(input())

def skill_check(number):
    point = []
    for i in str(number):
        point.append(i)

    mid = len(point)//2

    left_sum = sum(int(i) for i in point[:mid])
    right_sum = sum(int(i) for i in point[mid:])

    if left_sum == right_sum:
        print("lucky")
    else:
        print("ready")

skill_check(number)