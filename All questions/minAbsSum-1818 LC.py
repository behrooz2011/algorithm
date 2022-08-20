# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# min abs sum - LC 1818

def abso(nums1,nums2):
	sum=0
	obj={}
	for i in range(len(nums1)):
		sum += abs(nums1[i] - nums2[i])
		obj[i] = abs(nums1[i] - nums2[i])
	a = sorted(obj.items(), key=lambda x: x[1], reverse= True)
	print("sorted a:\t",a)
	indexNums2 =a[0][0]
	valueNums2 =nums2[indexNums2]
	print("valueNums2 from nums2:\t",valueNums2)
	newNum = nums1
	newNum.append(valueNums2)
	newNum.sort()
	print("newNum with the appended value:\t",newNum)
	ix =newNum.index(valueNums2)
	print("ix the new index referring to valueNums2:\t",ix)
	swap2 = 0
	if ix ==0:
	    #return(newNum[1])
	    swap2 = newNum[1]
	if ix == len(newNum)-1:
	    #return(newNum[ len(newNum)-2 ])
	    swap2 =newNum[ len(newNum)-2 ] 
	if abs(newNum[ix] - newNum[ix-1]) <= abs(newNum[ix] - newNum[ix+1]):
	    #return(newNum[ix-1])
	    swap2 = newNum[ix-1]
	else:
	    #return(newNum[ix+1])
	    swap2 = newNum[ix+1]
	return abs((sum - (a[0][1] -  (swap2 -valueNums2)) ))
print(abso(nums1 = [1,7,5], nums2 = [2,3,5]))
print(abso( nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10] ))
print(abso(nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]))
	
