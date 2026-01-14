def str_zip(s):
    answer = len(s)
    for step in range(1, len(s)//2+1): # 묶음 단위
        compressed = ""
        prev = s[0:step] # 비교 대상
        count = 1 # 묶음 개수
        for j in range(step, len(s), step):
            # 압축이 가능한 경우
            # prev를 그다음 묶음과 비교 ex) aabbaccc 에서 step=2고 prev가 aa면 bb와 비교 
            if prev == s[j:j+step]: 
                count += 1
            # 
            else:
                compressed +=  str(count) + prev if count >= 2 else prev
                prev = s[j:j+step] # 묶음 갯수만큼 이동
                count = 1
        # 남은 문자 처리
        compressed += str(count) + prev if count >= 2 else prev

        answer = min(answer, len(compressed)) # 가장 압축된 문자열의 길이 answer

    return answer


#"aabbaccc"