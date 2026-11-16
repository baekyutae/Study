'''
문자열 s가 주어졌을 문자열이 담긴배열 wordDict에 원소로 구분 가능한지 여부 t/f를 반환하는 함수를 만들어라
wordDict는 중복 사용가능

문자열 s에서 인덱스 i를 기준으로 s[:i] 가 wordDict로 구분 가능한지 알고 있다면
s[i+1:]가 wordDict로 구분되는지만 확인하면 됨
-> dp로 접근?

dp[i] : 문자열 s에서 s[:i]가 wordDict로 구분되는지 여부를  t/f 로 저장

start와 end두 인덱스를 운용
start는 end범위 내에서 wordDict로 구분이 보장된 범위가 존재하는지 즉 dp[start]가 존재하는지 탐색
-> 있다면 s[start:end]가 wordDict에 있는지만 확인하면 되니깐

end는 s에서 0부터 len(s)까지 이동해가며 len(s)까지 갔을때도 wordDict로 구분되는지 검증하는 역할을 함

start = 0
end가 1부터 시작해 s에서 이동하며 체크

0:end 범위 내에서
1. dp[start] == True이고
2. s[start:end]가 wordDict에 있는지 확인


바깥 for문에서 end가 이동하고
안쪽 for문에서 start는 0:end 범위내에서 이동해가며 단 하나라도 1,2조건을 충족하는 경우를 찾는다면

dp[end]를 true로 갱신 -> start중에 dp[start] == True가 있는지 탐색에 활용
안쪽 for문 종료

end+1해서 이동

----

시간복잡도
1. 바깥 for문 n
2. 안쪽 for문은 n-1만틈 반복
n회동안 매번 n-1만큼 반복하는게 아닌 n번째에서 안쪽에서 n-1번 반복하는거니

o(n)

공간복잡도
1. dp 공간
o(n)

----
edgecase

s ="aaaaaaa"
wordDict = ["aaaa","aaa"]
일때

start = end로 갱신하는 방식을 쓰니
start가 6일때 "aaa", "aaa" 즉 dp[6]까지 true지만 "a"하나가 남아 다음 반복회차인 end가 7일때 false가 나와버림(start가 6에서만 시작하니)
때문에 start가 0~7안에서 dp[start] == True면서 s[start:end]가 wordDict에 있는 경우를 찾게 만들어야 함 -> for start in range(0,end):

'''
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[0] = True

        wordSet = set(wordDict) # 존재 여부 체크시 최적화
        start = 0
        for end in range(1,len(s)+1):
            for start in range(0,end):
                if dp[start] == True and s[start:end] in wordSet:
                    dp[end] = True
                    break


        return dp[len(s)]
