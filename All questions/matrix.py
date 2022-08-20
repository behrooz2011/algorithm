# Rotate Matrix: Given an image represented by an NxN matrix,
#  where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. 
# Can you do this in place?

def matrix90(arr):
    result=[]
    
    for i in range(len(arr)):
        y =[]
        for j in range(len(arr)-1,-1,-1):
            y.append(arr[j][i])
        result.append(y)
        #y=[]
    return result
print(matrix90([
 ["a", "b", "c", "d"],
 ["e", "f", "g", "h"],
 ["i","j", "k", "l"],
 ["m", "n", "o", "p"]]))
 