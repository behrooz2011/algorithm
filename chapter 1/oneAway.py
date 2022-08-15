# One Away: There are three types of edits that can be performed on strings: 
# insert a character,
# remove a character, or replace a character.
#  Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
def oneAway(x,y):
    if len(x) == len(y):
        count = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                count += 1
        if count > 1:
            return False
        return True
    elif abs(len(x)-len(y)) == 1:
        obj1={}
        bigWord =""
        smallWorld=""
        if len(x) > len(y):
            bigWord = x
            smallWorld = y

        else:
            bigWord = y
            smallWorld = x
        
        for i in bigWord:
            obj1[i]=obj1.get(i,0)+1
        for letter in smallWorld:
            if letter not in obj1:
                return False
        return True
    
    else:
        return False
print(oneAway("apple","aple"))
print(oneAway("pale","bake"))
print(oneAway("pale","ale"))
print(oneAway("pale","bale"))
print(oneAway("pale","balee"))
print(oneAway("palee","bale"))
print(oneAway("palee","bale"))


## better solution / part 2 
## part one is similar 
def one_away(s1, s2):
    '''Check if a string can converted to another string with a single edit'''
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)
    return False


def one_edit_replace(s1, s2):
    edited = False
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True


def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True




    