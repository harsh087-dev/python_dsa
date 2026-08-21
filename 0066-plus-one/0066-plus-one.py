class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum=digits[0]
        result=[]
        for i in range(1,len(digits)):
            sum=sum*10+digits[i]
        sum=sum+1
        while sum>0:
            rem=sum%10
            result.insert(0,rem)
            sum=sum//10
        return result  