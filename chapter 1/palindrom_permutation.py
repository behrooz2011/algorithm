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


# pair comparison method
def check_permutation_by_sort(s1, s2):
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False
    return True

from collections import Counter
ll = ["a","b","a"]
c = Counter(ll)
for i in c:
    print(i)
for val in c.values():
    print(val)
print(c)

def is_palindrome_permutation_pythonic(phrase):
    """function checks if a string is a permutation of a palindrome or not"""
    counter = Counter(phrase.replace(" ", "").lower())
    return sum(val % 2 for val in counter.values()) <= 1
print(is_palindrome_permutation_pythonic("level"))
print(is_palindrome_permutation_pythonic("lebel"))
print(is_palindrome_permutation_pythonic("levell"))