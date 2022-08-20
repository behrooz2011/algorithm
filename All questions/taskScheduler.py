# Given a characters array tasks, representing the tasks 
# a CPU needs to do, where each letter represents a different task. 
# Tasks could be done in any order. Each task is done in one unit of time.
#  For each unit of time, the CPU could complete either one task or just be idle.

# However, there is a non-negative integer n that represents the 
# cooldown period between two same tasks (the same letter in the array), 
# that is that there must be at least n units of time between any two same tasks.

# Return the least number of units of times that the CPU will take to finish all the given tasks.
print('Hello, world!')
def cpuRest(arr,n):
  for i in range(len(arr)):
    if i+1 <len(arr) and arr[i] != arr[i+1]:
      continue
    else:
      for j in range(i+1,len(arr)):
        if arr[i] != arr[j]:
          arr[i+1],arr[j]=arr[j],arr[i+1]
          break
  # return arr
  print arr
  rest=0
  for i in range(len(arr)):
    if  i+1 < len(arr) and arr[i] == arr[i+1]:
      rest += n *(len(arr)-1-i)
      break
    else:
      return n+len(arr)
  return rest+ len(arr)
print(cpuRest(["a","a","a","b","b","b","c","c","c"],1))
print(cpuRest(["a","a","a","b","b","b"],1))