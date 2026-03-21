#Leet Code : 26. Remove Dupliceates from Sorted Array
#Link : https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]


def removeDuplicates(nums):
    # 원소가 0개 또는 1개면 그대로 반환
    if len(nums) <= 1:
        return len(nums)

    # write는 다음 unique 값을 써 넣을 자리
    write = 1

    # read는 앞에서부터 읽으면서 중복인지 확인
    for read in range(1, len(nums)):
        # 바로 앞 unique 값과 다르면 새로운 값이므로 앞쪽에 덮어쓰기
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1

    return write


k = removeDuplicates(nums)
print(k)          # 5
print(nums)       # [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
print(nums[:k])   # [0, 1, 2, 3, 4]


"""
핵심 아이디어
- 정렬되어 있으므로 중복 여부는 "이전 unique 값"과만 비교하면 된다.
- 진짜로 삭제(remove)할 필요는 없다.
- 앞쪽에 unique 값만 차례대로 덮어써 넣으면 된다.
- write가 곧 unique한 원소 개수 k가 된다.
"""