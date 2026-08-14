class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLen=len(s)
        tLen=len(t)
        sdict={}
        tdict={}
        if len(s)!=len(t):
            return False
        else:
            count=1
            for i in s:
                if i in sdict:
                     
                    sdict[i]+=count
                else:    
                   sdict[i]=count
            for j in t:
                if j in tdict:
                     tdict[j]+=count
                else:    
                     tdict[j]=count
        if sdict==tdict:
            return True
        else:
            return False      