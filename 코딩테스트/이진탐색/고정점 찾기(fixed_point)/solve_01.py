'''
반복문을 이용한 이진탐색

정렬된 수열에서 중간값과 그값의 인덱스를 비교 했을때
인덱스가 더 작다면?
오른쪽에 있는 모든 값듣은 인덱스보다 클것이므로 왼쪽만 탐색

인덱스가 더 크다면?
왼쪽에 있는 모든 값들은 인덱스 보다 작을 것이므로 오른쪽만 탐색

위 논리를 바탕으로 이진탐색을 수행해 모든 원소를 확인해보지 않아도 됨
'''

def fixed_point(n: int, num_list: list):
    
    start = 0
    end = n-1
        
    while start <= end:
        mid = (start+end)//2

        if mid == num_list[mid]:
            return mid

        elif mid >= num_list[mid]:
            start = mid + 1
        elif mid <= num_list[mid]:
            end = mid - 1

    return -1