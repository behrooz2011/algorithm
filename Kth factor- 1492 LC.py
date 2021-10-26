#kth factor
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        arr=[]
        for i in range(1,n+1):
            if n % i == 0:
                arr.append(i)
                if len(arr) == k:
                    return(arr[-1])
        return -1
        
# or:
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for x in range(1, n // 2 + 1):
            if n % x == 0:
                k -= 1
                if k == 0:
                    return x
        
        return n if k == 1 else -1
        #o(n) space complexity: o(1)