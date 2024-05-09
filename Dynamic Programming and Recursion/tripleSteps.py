""" Cracking the coding interview : DP and recursion chapter 8 """
""" Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can run up the
stairs. """

"Recursive - no DP"
def findStep(n):
    if ( n == 0 ):
        return 1
    elif (n < 0):
        return 0
 
    else:
        return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)

""" Bottom-up DP"""
def countWays(n):
    res = [0] * (n + 2)
    res[0] = 1
    res[1] = 1
    res[2] = 2
 
    for i in range(3, n + 1):
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]
 
    return res[n]
 
 
# Driver code
n = 4
print(countWays(n))

""" Top-Down DP - Memoization"""
# Python Program to find n-th stair using step size
# 1 or 2 or 3.
class GFG:

	def findStepHelper(self, n, dp):
	
		# Base Case
		if (n == 0):
			return 1
		elif (n < 0):
			return 0
			
		# If subproblems are already calculated
		#then return it
		if (dp[n] != -1):
			return dp[n]

		# store the subproblems in the vector
		dp[n] = self.findStepHelper(n - 3, dp) + self.findStepHelper(n - 2, dp) + self.findStepHelper(n - 1, dp)
		
		return dp[n]

	# Returns count of ways to reach n-th stair
	# using 1 or 2 or 3 steps.
	def findStep(self, n):

		dp = [-1 for i in range(n + 1)]
		return self.findStepHelper(n, dp)

# Driver code
g = GFG()
n = 4

print(g.findStep(n))

# This code is contributed by shinjanpatra.
