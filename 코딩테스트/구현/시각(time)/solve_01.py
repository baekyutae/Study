# 완전 탐색(Brute Force)
# 시간복잡도 O(N) => 시간 h * 3600(초*분)

h = int(input())

def number_check(h):
    count = 0
    for i in range(0,h+1):
        for m in range(60):
            for s in range(60):
                if '3' in str(i)+str(m)+str(s):
                    count += 1
    return count

number_check(h)