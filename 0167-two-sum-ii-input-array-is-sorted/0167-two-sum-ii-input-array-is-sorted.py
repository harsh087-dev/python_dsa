class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while left<right:
            sumofdig=numbers[left]+numbers[right]
            if sumofdig ==target:
                return [left+1,right+1]
            if sumofdig>target:
                right-=1
            else:
                left+=1               