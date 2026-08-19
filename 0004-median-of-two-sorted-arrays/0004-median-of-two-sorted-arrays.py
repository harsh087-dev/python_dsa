class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        nums=sorted(nums)
        numLen=len(nums)
        if numLen%2==0:
            num1=numLen//2
            num2=numLen//2-1
            median=(nums[num1]+nums[num2])/2
        else:
            median=nums[numLen//2]
        return median            