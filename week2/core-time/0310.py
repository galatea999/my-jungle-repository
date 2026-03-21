
"""
 숫자의 갯수만큼 탐색, 숫자 하나당 3개가 가능함. 이 3개를 어디 저장하지
숫자마다 정해진 글자 3개 탐색 후 output에 추가하고 return
Backtracking의 3요소 선택 탐색 삭제 
"""
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/?envType=study-plan-v2&envId=top-interview-150

def handy_combination(digits) :
    mapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
    
    

    result = []
#핵심은 현재 몇번째 숫자를 처리중인지를 인덱스로 넘기는 것
    def backtracker(index, current_list) : #index
        
        #Base case
        if index == len(digits) :
            result.append(''.join(current_list))
            return

        current_digit = digits[index] # digit중 현재 문자만 뽑음
        for ch in mapping[current_digit] : #이중으로 선택되는 구조. 여기가 좀 어려웠음
            current_list.append(ch) # 선택
            backtracker(index+1, current_list) # 탐색
            current_list.pop() #삭제 

    backtracker(0,[]) # 조합에선 1을 넘겨줬었는데 => 생각해보니 조합에서 1도 인덱스(깊이)
    return result

print(handy_combination("23"))
      

