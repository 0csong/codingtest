def solution(s, skip, index):
    answer = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz" # 알파벳
    
    for ch in skip: # ch => skip의 문자 하나하나
        if ch in alpha:
            alpha = alpha.replace(ch, "") # 알파벳 안에 skip 문자들 제거
    
    for i in s:
        
        change = alpha[(alpha.index(i) + index) % len(alpha)] # s의 문자 인덱스 + index를 alpha의 길이로 나눈 나머지를 알파벳으로 변환
        answer += change
    
    return answer

## 1. 먼저 skip에 있는 문자들을 제거함
## 2. 이후 index를 더해서 해당 문자를 찾음
## 3. 만약 문자열 길이를 초과할 경우를 위해 len(alpha)로 나누어 나머지의 인덱스를 구함(초과할 경우 다시 a부터 시작하게 되어있음)
