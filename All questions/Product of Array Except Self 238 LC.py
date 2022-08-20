#Product of Array Except Self// Division is not allowed
#https://leetcode.com/problems/product-of-array-except-self/discuss/1597994/C%2B%2B-3-Simple-Solutions-w-Explanation-or-Prefix-and-Suffix-product-O(1)-space-approach
import math
def productExceptSelf(nums):
    newNum = nums.copy()
    arr = []
    for i in range(len(nums)):
        newNum.pop(i)
        arr.append(math.prod(newNum))
        print("newNum: ",newNum)
        newNum = nums.copy()
        print("new Num 2 after copy:",newNum)
    return arr
print(productExceptSelf([1,2,3,4]))
# Time Limit Exceeded

#solution 2/ 3 loops O(3n) = O(n)
def pro(nums):
    list1=[]
    prod = 1
    for i in range(len(nums)-1,-1,-1):
        print("i:",i)
        prod *= nums[i]
        list1.append(prod)
    print("list1: ",list1)
    
    list2=[]
    prod = 1
    for i in range(len(nums)):
        prod *= nums[i]
        list2.append(prod)
    print("list2: ",list2)
    
    list3 = []
    prod = 1
    for i in range(len(nums)):
        if i == 0:
            list3.append( list1[len(nums)-i-2] )
        elif i == len(nums)-1:
            list3.append(list2[-2])
        else:
            list3.append(list2[i-1]* list1[len(nums)-i-2])
    
        
    return list3
print(pro([10, 2, 3, 4, 5]))

#Solution3
def productExceptSelf(nums):
    

    # T: O(n), S: O(1)
    res, prod = [0] * len(nums), 1
    for i in range(len(nums)):
        res[i] = prod
        prod *= nums[i]

    prod = 1
    for i in range(len(nums) - 2, -1, -1):
        prod *= nums[i + 1]
        res[i] *= prod
    return res

