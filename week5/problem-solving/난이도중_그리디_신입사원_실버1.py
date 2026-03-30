# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946


"""

지원자의 숫자 1<= N <= 10^5 


인풋 a(서류), b(면접)
a b 둘 중에 하나라도 최저점을 갱신하면 탈락. 아니구나.

a에 대한 결과값 True False,
b도 마찬가지
result_a or result_b == 합격

아니지 아니지, 그렇게 할 필요 없지. Early Return 때리면되지.
만약 a 결과값이 True이면 return 합격
a가 아니더라도, b 결과값이 True이면 return 합격
함수의 끝 return 불합격

idea
반대로 생각해보자.
a,b 중 적어도 하나가 다른 지원자보다 떨어지지 않는사람만 선발
=> a, b가 둘 다 "상대 우위"가 없으면 탈락.

드모르간에 의해 같은 말이긴 하지만, 둘 중에 뭐가 더 코드로 쓰기 편할까?

걍 전자로 해보자. 코드 틀은 짜놨으니까

2) 상대우위를 어떻게 검증하느냐
"다른 모든 지원자랑 비교"
떨어지지 않는 자. 즉, a가 다른 모든 지원자들보다 같거나 큰 사람
그러면 a기준으로 했을때 탈락자(기준자)는 적어도 1명 (동점자면 여러명)
b기준으로도 적어도 탈락자(기준자)는 적어도 1명 (동정자면 여러명)
즉, 탈락자를 뽑아내는게 빠름. a와 b 기준으로 모든 지원자들보다 작은 사람
근데 이런사람 없는데?

~ (a or b) = ~ a and ~ b 인데.

아 미친. 문제를 끝까지 읽어야지. 점수가 아니라 순위였구나.
순위일때는 뭐가 달라지지?

'최대'인원수? 왜 최대란 말이 나오지? 경우의 수가 한가지 아닌가?

이게.. 모든 인원을 각각 비교를 해야하나? 

탈락자 판별을 한다고 해보자.
이게 전체를 돌면서 한명이라도.. 아 이러면 또 너무 비효율적인데



그리디를 적용해서 생각해보면? 그 순간에 최선에 판단이느냐? 

한놈하고만 비교하고 판별해도 되냐? 되지. 합격인 경우에는. 불합격은 끝까지 가야하고. 그게 그리디라면 그리디라고 표현할 필요가 있나?


에라 모르겠다 답지를 보자 잠깐 쉬고.

왜 못 풀었느냐? => 문제 이해 자체를 못 함 



test_case = int(input())

result = []
while test_case :

    num = int(input())
    cases = []
    for _ in range(num) :
        cases.append(list(map(int, input().split())))

    cases.sort(key = lambda x:x[0])

    #탈락자 결정 세션
    hire_count = len(cases)    
    for i in range(1, len(cases)) : #탈락자 후보
        for j in range(0, i) : #비교군
            if cases[i][1] > cases[j][1] :
                hire_count -= 1
                break
    

    result.append(hire_count)
    test_case -= 1

for ch in result :
    print(ch)

"""
test_case = int(input())
result = []
for _ in range(test_case):
    num = int(input())
    cases = []
    for _ in range(num):
        cases.append(tuple(map(int, input().split())))

    cases.sort(key=lambda x: x[0])

    hire_count = 1
    best_interview = cases[0][1] #초기값 설정후 계속 갱신

    for i in range(1, len(cases)):
        if cases[i][1] < best_interview:
            hire_count += 1
            best_interview = cases[i][1]

    result.append(hire_count)

for ch in result:
    print(ch)


    """
    나보다 서류도 좋고 면접도 좋은 사람이 한 명이라도 있으면 탈락.
    처음에 best_interview를 정해놓고 하면 안되는 이유
    전체 지원자 중 최고 면접이 아니라, 
    앞에서부터 보면서 갱신되는 값이여야함. 
    왜냐면 탈락조건이 나보다 '면접 좋은 사람이 앞에 있어야함' 이기 때문.

    

  에이씨.. 앞으로 이걸 논리기호로 바꾸는 연습을 하자. 조건만 잘 정하고 논리기호 잘 쓰면 훨씬 도움이 될듯.

힌트를 보고 나서 : 왜 못 풀었던 것 같아?
=> 보고나면 늘 허무함. 쉽게 풀려서. 왜 저렇게 생각을 못 했는지를 고민해야겠지.
아이디어는 무엇이고, 이게 왜 Greedy 알고리즘인가?

내가 막힌 이유
1) "각 사람마다 다른 모든 사람과 비교해야 하나?" 
!!! 알고리즘은 원문 조건을 그대로 구현하면 인된다. 같은 뜻을 더 싼 형태로 번역하는 것이다.

2) !!! 2차원 비교, 즉 비교 조건이 여러개가 나오면 정렬을 강하게 의심해 봐야 한다.
=> 정렬로 한 축을 없앨 수 있지 않을까? 

3) 존재여부를 '대표값 하나'로 압축하는 감각
"앞 사람들 중에 면접이 나보다 더 좋은 사람이 하나라도 있나?"
=> 여기서 앞 사람 전부 봐야지가 아니라, 그 집합의 최강 하나만 보겠네.  

∃ j : doc[j] < doc[i] and interview[j] < interview[i]

"존재?"가 나오면 대표값으로 압축이 가능한지 보기.


A and B 꼴로 쓴다.
그다음 바로 묻는다.

“A를 정렬로 자동화할 수 있나?”
가능하면 B만 남는다.
그다음엔
“B는 누적 최소/최대 하나로 대표 가능하나?”


??? 이것이 왜 그리디였는가?

현재까지의 정보를 대표하는 값 하나만 유지하면, 미래 판단에 충분한가 ? 
!!! 그리디란 매 순간의 국소적인 판단이 전체 최적해를 망치지 않는 경우.
    """