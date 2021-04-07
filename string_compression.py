# X is the input string
def stringCompression(x):
  obj={}
  string1=""
  for letter in x:
    obj[letter]=obj.get(letter,0)+1
    # if letter not in obj:
    #   obj[letter] =1
    # else:
    #   obj[letter] += 1
  print(obj)
  
  for letter in x:
    if letter in string1:
      continue
    if obj[letter] != 1:
      
      string1 +=letter + str(obj[letter])
    else:
      string1 += letter
  print(string1)
  
stringCompression("permanent")
stringCompression("hello")
stringCompression("baby")
stringCompression("wwwwaaab")

#another one acooding to the book's example
print('Hello, world!')
def compress_string(string):
    compressed = []
    counter = 0

    for i in range(len(string)):  # noqa
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    if counter:
        compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    print("this is the result:","".join(compressed))
    return min(string, "".join(compressed), key=len)
print(compress_string("hello"))
print(compress_string("permanent"))
print(compress_string("aabcccccaaa"))