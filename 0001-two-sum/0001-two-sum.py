class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index,num in enumerate(nums):
            digit=target-num
            if digit in seen:
                return [seen[digit],index]
            seen[num]=index    