# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

case_count = int(input()) #백준 참 까다롭다. 인풋 문구도 쓰지 말래
for c in range(case_count):
    data = list(map(int, input().split())) #map()
    student_number = data[0]
    average = 0
    scores =data[1:]
    sum_scores = 0
    for i in range(student_number) :
        sum_scores += scores[i]

    # 평균
    average = sum_scores / student_number

    #평균을 넘는 학생들 판별
    over_average_num = 0

    for i in range (student_number) :
        if scores[i] > average :
            over_average_num += 1 
    result = over_average_num / student_number
    print(f"{result:.3%}") # f-string으로 :.n%로 처리하면 알아서 퍼센티지로 나오고, 소숫점 n번자리까지 표시