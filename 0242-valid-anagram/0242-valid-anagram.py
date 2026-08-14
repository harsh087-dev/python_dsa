class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict={}
        tdict={}
        if len(s)!=len(t):
            return False
        else:
            for i in s:
                sdict[i]=sdict.get(i,0)+1
            for j in t:
                tdict[j]=tdict.get(j,0)+1
        if sdict==tdict:
            return True
        else:
            return False      