class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in nums:
            if i in dict:
                return True
                break
            dict[i]=1    
        return False        