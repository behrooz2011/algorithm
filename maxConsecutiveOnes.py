
# Given a binary array, find the maximum number of
#  consecutive 1s in this array.

# Example 1:
# Input: [1,1,0,1,1,1]
# Output: 3

# def ones(x):
#     obj={}
#     for i in range(len(x)):

#         if x[i]== 1:
#             obj[i] = 1
#         if i+1 < len(x) and x[i] == x[i+1] and x[i+1] == 1:
#             obj[i] += 1
#         # MaxKey = max(obj, key=obj.get)
#     return obj
# print(ones([1,1,0,1,1,1,1]))

def ones(arr):
    obj = {}
    for i in range(len(arr)):
        if arr[i] == 1:
            obj[i] =1
            for j in range(i, len(arr)):
                if j+1 < len(arr) and arr[j] == arr[j+1]:
                    obj[i] += 1
                else:
                    break
    MaxKey = max(obj, key=obj.get)
    return obj[MaxKey]
print(ones([1,1,0,1,1,1,1,9,9,1]))

#better solution
class Solution:
    def findMaxConsecutiveOnes(self, x: List[int]) -> int:
          count = 0
          compare=0
          for i in range (len(x)):
            if x[i]==1:
              count +=1
            else:
              compare= max(compare,count)
              count = 0
          return(max(compare,count))
print(ones([1,2,1,1,1,0,3,2,1,1,1,1,1,3,1]))
print(ones([1,1,2,0,1,1,1,9,1]))
print(ones([1,0,1,1]))