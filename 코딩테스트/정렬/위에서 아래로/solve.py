'''
입력된 숫자를 배열에 저장

배열을 오름차순으로 정렬

졍렬된 배열을 순회하며 공백으로 구분 하며 출력

'''


n = int(input())
number = []

for _ in range(n):
    number.append(int(input()))

def up_to_down(number):
    sort_number = sorted(number, reverse=True)

    for i in sort_number:
        print(i, end= ' ')

up_to_down(number)