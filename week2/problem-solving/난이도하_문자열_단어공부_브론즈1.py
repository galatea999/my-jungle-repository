# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
"""
어떤 알파벳이 가장 많이 사용되었는지?
"""

#str
word = input().upper()

current_most = ["", 0]
done_alphabet = []
for ch in word :
    if ch in done_alphabet :
        continue
    number_count = word.count(ch)
    if number_count > current_most[1] :
        current_most[0] = ch
        current_most[1] = number_count
    
    elif number_count == current_most[1] :
        current_most[0] = "?"

    done_alphabet.append(ch)

print(current_most[0])
    # 한 글자를 한번만 셀 수 있는 방법. 이미 센 적이 있으면 skip
