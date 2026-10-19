class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countd= {}
        for a,b in zip(s,t):
            countd[a]=countd.get(a,0)+1
            countd[b]=countd.get(b,0)-1
        for count in countd.values():
            if count!=0:
                return False
        return True
    

        
