class Solution:
    def leastBricks(self, x: List[List[int]]) -> int:
      summ = 0
      for i in range(len(x)):
        for j in range(len(x[i])):
          summ += x[i][j]
          if j>0 :
            x[i][j] += x[i][j-1]
      if summ == len(x):
        return len(x)
    #   print(x)
    # brickWall([ [1,2,2,1], [3,1,2], [1,3,2], [2,4], [3,1,2], [1,3,1,1] ])
      counter =0
      result=[]
      for i in range(1,x[0][-1]):
        for j in range(len(x)):
             if i not in x[j]:
               counter += 1
        result.append(counter)
        counter = 0 
      return(min(result))