class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict={}
        left=0
        window={}
        for i in s1:
            dict[i]=dict.get(i,0)+1
        for right in range(len(s2)):
            window[s2[right]]=window.get(s2[right],0)+1
            if right-left+1>len(s1):
                window[s2[left]]-=1
                if window[s2[left]]==0:
                    del window[s2[left]]
                left+=1
            if window==dict:
                return  True        
        else: 
            return False    