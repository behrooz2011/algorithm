# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def palperm(x):
    count=0
    obj={}
    y= sorted(x)
    print(y)
    for i in range(len(y)):
        if y[i] not in obj:
            obj[y[i]] = 1
            if i-1 > -1 and (obj[y[i-1]] % 2 == 1):
                count += 1
                print("this obj[y[i-1]]: ",obj[y[i-1]])
        else:
            obj[y[i]] += 1
    print("this is obj:",obj)
    # print("this is count:",count)
    if count + (obj[y[0]] % 2)  + (obj[y[len(y)-1]] % 2) > 1:
        # print (count + (obj[y[0]] % 2))
        print (count)
        print (obj[y[0]]%2)
        return False
    else:
        return True
print(palperm("ellv"))
print(palperm("level"))
# print(palperm("radar"))
# print(palperm("defied"))
# print(palperm("rotor"))
# print(palperm("roor"))
print(palperm("lebel"))
# print(palperm("levelv"))
# print(palperm("hll"))
# print(palperm("hi"))


## correct approach ##
def pali(x):
    obj={}
    counter = 0
    for index,val in enumerate(sorted(x)):
        if val not in obj:
            obj[val]=1
        else:
            obj[val] += 1
    # print(obj)
    for value in obj:
        if obj[value] % 2 == 1:
            counter += 1
    if counter > 1:
        return False
    return True
print(pali("level"))
print(pali("lebel"))
print(pali("ellv"))
print(pali("ellv"))
