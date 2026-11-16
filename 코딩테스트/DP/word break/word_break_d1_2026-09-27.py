'''
주어진 단어 s를 사전 wordDict에 있는 단어로 띄워쓰기 단위로 구분가능한지 t/f 반환

<알고리즘 접근 과정>
s에서 index 0부터 시작해서  i 를 기준으로 0~i-1 범위가 wordDict로 구분 가능한지를 확인
s끝까지 구분 가능하다면 출력이 true로 나오겠지

index가  5일때 index 2 일때 0~1 범위가 구분 가능한지 확인했으면 또 할필요 없이 2~4 범위가 구분가능한지만 확인하면됨

즉 구분가능여부를 저장해둔다 -> dp로 접근 가능


dp라면 점화식을 세우는게 핵심
dp[i]는 s에서 0~i-1 범위의 문자열이 wordDict로 구분가능한지를 저장한다

dp[i] = dp[start] + s[start:end] in set(wordDict)
즉 0~end-1 범위 내에서 start로 잘랐을때 true인 영역이 존재하고 나머지 영역이 wordDict로 구분 가능하다면 

dp[i]도 true

start 값은 여러개가 존재가능하며 대입해보며 확인, 하나라도 찾으면 더 찾을 필요가 없다

<시간복잡도>
1. for문 바깥: s의 길이 n
2. for문의 안쪽: 최악의 경우 n
3. 문자열 슬라이싱: 최악의 경우 문자길이는 n
o(n^3)

공간복잡도
o(n)

<edge case>
1. 시간복잡도 최악: 2700만이라 에러 안남
2. s와 wordDict이 한글자로만 이루어진 경우 "aaaaa" , ["a","aa"] : 테스트 케이스 돌려보니 True 잘 나옴
"aaaaa" , ["aaaaaaa"] 는 False

'''

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # dp에 저장되는게 dp[i]일때 i-1까지 범위의 문자열이 구분 가능하지 이므로 갯수는 +1해줌
        dp = [False]*(len(s)+1)
        wordSet = set(wordDict)

        # 점화식 성립을 위해 dp[0]은 true로 둠
        dp[0] = True

        # index 0 부터 7 까지 dp[i]를 저장:
        for end in range(1,len(s)+1):
            # end 범위 내에서 자르기를 할 start
            for start in range(end):
                if dp[start] and s[start:end] in wordSet:
                    dp[end] = True
                    break

        return dp[len(s)]
