class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[]
        arr2=[]
        arr1.append(nums[0])
        arr2.append(nums[1])
        result=[]
        last_index1=0
        last_index2=0
        for i in range(2,len(nums)):
            if arr1[last_index1:]>arr2[last_index2:]:
                arr1.append(nums[i])
                last_index1+=1
            else:
                arr2.append(nums[i])
                last_index2+=1
        result=arr1+arr2
        return result            