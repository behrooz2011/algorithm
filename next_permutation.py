#next permutation

# Implement next permutation, which rearranges numbers 
# into the lexicographically next greater permutation of numbers.
# If such an arrangement is not possible, it must rearrange it as 
# the lowest possible order (i.e., sorted in ascending order).
# The replacement must be in place and use only constant extra memory.

print('Hello, world!')
def nextPerm(x):
  n = len(x)
  y = sorted(x,reverse=True)
  print("this is the list with a descending order :",y)
  if x == y:
    x.sort()
    return x
    
  for i in range(n-1 , -1, -1):
    if (i-1 > -1 and x[i] < x[i-1]) or (i-1 > 1 and x[i]==x[i-1]):
      continue
    else:
      sub1 = x[:i] 
      sub2 = x[i:n]
      sub2.sort()
      for j in range(len(sub2)):
        if i-1 > -1 and  sub1[i-1] < sub2[j]:
          tt = sub1[i-1]
          sub1[i-1]= sub2[j]
          sub2[j] = tt
          sub1.extend(sub2)
          return sub1
        
print(nextPerm([1,2,3]))
print(nextPerm([2]))
print(nextPerm([2,3,6,5,1]))
print(nextPerm([5,4,0]))