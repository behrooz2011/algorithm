
# Given an unsorted array of integers nums, 
# return the length of the longest consecutive elements sequence.

 
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
print('Hello, world!')

def long(x):
  x.sort()
  if x == []:
    return 0
  count=1
  compare = 0
  for i in range (len(x)):
    if i+1 < len(x) and x[i]==x[i+1]-1:
      count += 1
    elif i+1 < len(x) and x[i]==x[i+1]:
      continue
    else:
      compare = max(compare, count)
      count = 1
      print("here's compare:",compare)
  return(max(compare, count))
print(long([1,2,500,300,4,4,6,5]))
print(long([100,4,200,1,3,2]))
print(long([2]))
print(long([2,4,6]))
