class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        sum=0
        min_len=len(nums)+1
        count=0
        while right<len(nums):
            sum=sum+nums[right]
            while sum>=target:
                min_len=min(min_len,right-left+1)    
                sum-=nums[left]
                left+=1
           
            right+=1
        return 0 if min_len == len(nums) + 1 else min_len           
               




        