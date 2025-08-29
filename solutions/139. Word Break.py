class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words=set(wordDict)
        memo=[-1]*len(s)
        def check(s,st,end):

            if st>=len(s):
                return True

            if end>len(s):
                return False

            if memo[st]!=-1:
                return memo[st]

            branch1=False
            if s[st:end] in words:
                branch1=check(s,end,end+1)

            branch2=check(s,st,end+1)
            memo[st]=branch1 or branch2
            return memo[st]
        return check(s,st=0,end=1)


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words=set(wordDict)
        memo=[False]*(len(s)+1)
        memo[len(s)]=True
        def check(s):
            for i in range(len(s)-1,-1,-1):
                # print(i)
                for j in range(i+1,len(s)+1):
                    # print(i,j)
                    if s[i:j] in words and memo[j]:
                        memo[i]=True
            return memo[0]
                
        # print(memo)
                
        return check(s)