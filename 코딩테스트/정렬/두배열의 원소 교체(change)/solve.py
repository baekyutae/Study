
'''
a의 작은 값들을 b의 더 큰값들로 순서대로 교체

a의 배열은 오름차순
b의 배열은 내림차순
정렬

index 0 부터 k-1 까지 두 배열 원소 교환
a의 원소보다 b의 원소가 큰경우에만 교환

a배열속 원소들의 합

'''
def element_change(a,b,k):
    sorted_a = sorted(a)
    sorted_b = sorted(b, reverse=True)
    
    for i in range(k):
        if a[i] < b[i]:
            sorted_a[i] = sorted_b[i]
        else:
            break
    return sum(sorted_a)

