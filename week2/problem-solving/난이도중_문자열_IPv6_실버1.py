# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

#축약형 IPv6가 주어졌을때, 이를 원래 IPv6(32자리의 16진수)로 복원하는 프로그램
"""
IPv6가 만들어진 역순으로 하면 되겠지.
IPv6가 어떻게 만들어졌는가?
1) 앞자리의 0,혹은 0으로만 이루어진 경우 0을 전체 또는 일부 생략 가능
2) if 0으로만 이루어진 연속된 그룹(갯수는 상관없음) => ::로 바꿀 수 있음 (한번만)

그러면 역순은?
1) :: => 0000:0000 으로 바꾸기. 근데 몇개가 빈지 알아야할듯. 총 글자수 세보고 비교?
2) 네자리가 아닌 것들은 앞에 0을 추가 

머야. 걍 숫자 빠진거 있으면 0이잖아? 0 몇개 추가할거냐 이거네?
잘개잘개 쪼개보자.. 결국 순서. 로직.


대원칙 : ":"을 기준으로 끊어서 보는 것. 4개가 아니면 앞에 4개가 되게 0을 추가해줌.
마지막에 다시 붙이면 되겠네.
":"의 총 갯수는 7개. 만약 7개가 아니고, ::가 존재한다면? 0000을 채울 때인데?
::가 있으면 :의 갯수가 7개가 아님!!! 일단 케이스 빼는 법은 찾음. 
"""

ipv6 = input() # 총 39글자

blank = []
if len(ipv6.split(":")) < 8 : #  ::이 존재할 때  
    #리스트의 원소 갯수를 8개로 만들어줘야함
    arg1 = ipv6.split("::") #스플릿을 하고, 다시 왼쪽 오른쪽으로 나누기. 
    left = arg1[0].split(":") #리스트 갯수 파악을 위해 왼쪽 스플릿하기
    right = arg1[1].split(":") #리스트 갯수 파악을 위해 오른쪽 스플릿하기
    number_of_arg = len(left) + len(right)
    while number_of_arg < 8 :
        blank.append('')
        number_of_arg += 1
    ipv6 = left + blank + right
    # print(ipv6)
    
    
else :
    ipv6 = ipv6.split(":")

full_ipv6 = []
for seg in ipv6 :
    if len(seg) < 4 :
        seg = seg.zfill(4)
    full_ipv6.append(seg)

full_ipv6 = ":".join(full_ipv6)
print(full_ipv6)