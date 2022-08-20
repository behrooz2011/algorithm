# Given an array of strings words, return the words that can be typed 
# using letters of the alphabet on only one row of American keyboard like the image below.

# In the American keyboard:

# the first row consists of the characters "qwertyuiop",
# the second row consists of the characters "asdfghjkl", and
# the third row consists of the characters "zxcvbnm".


# Example 1:

# Input: words = ["Hello","Alaska","Dad","Peace"]
# Output: ["Alaska","Dad"]
# Example 2:

# Input: words = ["omk"]
# Output: []
# Example 3:

# Input: words = ["adsdf","sfd"]
# Output: ["adsdf","sfd"]
def keyboard_row(words):
    row1= "qwertyuiop"
    row2 = "asdfghjkl"
    row3 = "zxcvbnm"
    arr =[]

    for i in range(len(words)):
        y=""
        #finding which row each letter belongs to and assigning it to the empty variable y
        for j in range(len(words[i])):
            if words[i][j] in row3:
                y = row3
            if words[i][j] in row2:
                y = row2
            if words[i][j] in row1:
                y = row1
            if words[i][len(words[i])-1] not in y:
                 print(f"last letter not found in y: {words[i][len(words[i])-1]}")
            

            if  (j+1 < len(words[i]) and words[i][j+1] not in y ):
                break
            elif words[i][len(words[i])-1] not in y:
                break
            else:
                continue
            arr.append(words[i])
    return arr
print(keyboard_row(["dad","alaska","peacre"]))
print(keyboard_row(["peace"]))
print(keyboard_row(["man"]))
        

