# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

case_number = int(input())

for c in range(case_number) :
    raw_input = input().split() #띄어쓰기를 기준으로 리스트 형식으로 받아짐
    iter_num = int(raw_input[0]) #3
    iter_str = raw_input[1] #ABC
    result_list=[]
    for ch in iter_str :
        result_list.append(ch*iter_num)
        result_str = "".join(result_list) 

    

    print(result_str)