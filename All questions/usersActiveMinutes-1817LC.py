#1817. Finding the Users Active Minutes (LC)

from collections import Counter
# from collections import Counter
# obj ={"a":2,"b":2,"c":3,"d":2, "e":2}
# print(Counter(obj.values())[2])
def section( logs,k ):
    obj={}
    arr=[]
    res=[]
    for x in logs:
    	if x[0] not in obj:
    	    obj[ x[0] ] = 1
    	    arr.append(x)
    	if x not in arr:
    	    obj[x[0]] += 1
    	    arr.append(x)
    print("this is the final unique array:\t",arr)
    print("this is the obj:\t",obj)
    for i in range(k):
       res.insert(i,Counter(obj.values())[i+1])
    print("res:\t",res)
    return(obj)

print(section( [[0,5],[1,2],[0,2],[0,5],[1,3]],5 ))
print(section( [[1,1],[2,2],[2,3]],4 ))