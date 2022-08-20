#696. Count Binary Substrings
class Solution(object):
    def countBinarySubstrings(self, s):
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans
#second approach (Brute force)
print("Hello world")
def x(s):
    arr=[]
    sum = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            arr.append(s[i:j])
    print(arr)
    for i in range(len(arr)):
        if arr[i].count("0") == arr[i].count("1"):
            print("hi sub",arr[i][0: (len(arr[i]))//2 ])
            if len( set(arr[i][0:(len(arr[i]))//2]) ) ==1:
                sum += 1
    return(sum)
    
print(x("1100"))
print(x( "110001111000000" ))