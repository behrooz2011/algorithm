print("Hello world")
class Solution:
    res = []
    def isPal(self,s):
        if s ==s[::-1]:
            self.res.append(s)
           
    def longestPalindrome(self, s: str) -> str:
        print("S:",s)
        # ss=""
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                self.isPal(s[i:j])
       
        self.res.sort(key=len)
        print("res:",self.res)
        return self.res[-1]
print(Solution().longestPalindrome("cbbd"))