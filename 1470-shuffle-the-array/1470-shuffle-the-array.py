class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arrLen=len(nums)//2
        result=[]
        for i in range(0,arrLen):
            result.append(nums[i])
            result.append(nums[i+arrLen])
        return result    

