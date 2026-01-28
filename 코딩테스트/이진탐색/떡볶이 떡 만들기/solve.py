'''
떡의 길이가 10억이므로 0부터 전수 조사할시 시간제한 2초 초과
절단기의 길이는 가장 긴떡 보다 작아야한다(크면 자른 떡 길이가 모두 0)

=> 0 ~ max(떡길이) 사이에서 잘린떡 길이의 합 total 과 요청한 떡 길이 m 이 같게 만드는  절단기 길이를 탐색

이진탐색 수행

'''


n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))


start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1
    else:
        result = mid # m이상의 떡을 제공하는 절단기의 높이, 최종적으론 m만큼 떡을 자르는 절단기의 높이
        start = mid + 1

print(result)