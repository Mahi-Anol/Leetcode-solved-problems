class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        else:

            a=[0]*26

            verifier=0
            for i in range(len(s)):
                a[97-ord(s[i])]+=1
                a[97-ord(t[i])]-=1
            
            for i in range(len(a)):
                if a[i]!=0:
                    return False
            
            return True

