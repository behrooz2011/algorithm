# Implement an algorithm to determine if 
# a string has all unique characters. What if you
# cannot use additional data structures?
def isUniq(x):
    #with additional data structure:
    obj={}
    for i in range(len(x)):
        if x[i] in obj:
            return False
        obj[x[i]]=x[i]
    return True
print(isUniq([1, 2, 5, -1, 0, 9]))
print(isUniq([1, 2, 5, -1, 0, 5, 77]))
print(isUniq("hi dear")) 
print(isUniq("hi dear jol")) 



#Testing 
def isUniq_NoAdditionalData(x):
    # y= sorted(x,reverse=True) in a descending order
    # y= sorted(x)
    # z ="".join(y)
    return "".join(sorted(x))
print(isUniq_NoAdditionalData("hello"))
print(isUniq_NoAdditionalData("hello guys!"))



# Now without additional data structure

def isUniq_NoAdd(x):
    for i in range(len(x)):
        if i+1 <len(x) and "".join(sorted(x))[i]=="".join(sorted(x))[i+1]:
            return False
    return True
print(isUniq_NoAdd("hello"))
print(isUniq_NoAdd("hello guys!"))
print(isUniq_NoAdd("my car"))
