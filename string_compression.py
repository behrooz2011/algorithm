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