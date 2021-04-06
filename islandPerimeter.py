# You are given row x col grid representing a map where grid[i][j] = 1 represents land 
# and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island 
# (i.e., one or more connected land cells).

# # The island doesn't have "lakes", meaning the water inside isn't connected to
#  the water around the island. One cell is a square with side length 1. 
# The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

class Solution:
    def islandPerimeter(grid):
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                upNeighbor=0
                downNeighbor = 0
                leftNeighbor = 0
                rightNeighbor = 0

                if grid[i][j] == 1:
                    if(i-1> -1):
                        # print("this is g[i-1]",grid[i-1][j])
                        upNeighbor = grid[i-1][j]
                    if(i+1 < len(grid)):
                        # print("this is g[i+1]",grid[i+1])
                        downNeighbor = grid[i+1][j]
                    if(j-1 > -1):
                        leftNeighbor = grid[i][j-1]
                    if(j+1 < len(grid[i])):
                        rightNeighbor = grid[i][j+1]
                    res += 4- (upNeighbor + downNeighbor + leftNeighbor + rightNeighbor)
        return res
print(Solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(Solution.islandPerimeter([ [0,0,0,0], [1,1,1,0], [0,1,0,0], [1,1,1,0] ] ))
# print(Solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(Solution.islandPerimeter([ [0,0,0,0], [0,1,1,0], [0,1,1,0], [0,0,0,0]] ))





