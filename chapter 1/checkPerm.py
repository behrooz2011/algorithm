# Check Permutation: Given two strings, write a method 
# to decide if one is a permutation of the
# other.
import unittest
def checkPerm(x ,y):
    if len(x) != len(y):
        return False
    if sorted(x) == sorted(y):
        return True
    else:
        return False
# print(checkPerm("abcd","dcba"))
# print(checkPerm("abcd","dcfa"))
# print(checkPerm("",""))
# print(checkPerm("abcd","dcbaa"))
print(checkPerm("dog","dog"))
###########################################
###############################
###############################
###############################

test2 = [
        ["dog", "god", True, "hi"],
        ["abcd", "bacd", True,"good"]
]
for str1, str2, ex, y in test2:
  print (str1,str2,y)

print('Hello, world!')
test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )
# for str1, str2, expected in test_cases:
#   print(str1,str2,expected)

test1 = [
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
]
print("kkkkkkk")
# for str1, str2, expected in test1:
#   print(str1,str2,expected)

###############################
###############################
###############################

class Test(unittest.TestCase):
    test_cases1 = (
            ("dog", "god", True),
            ("abcd", "bacd", True),
            ("3563476", "7334566", True),
            ("wef34f", "wffe34", True),
            ("dogx", "godz", False),
            ("abcd", "d2cba", False),
            ("2354", "1234", False),
            ("dcw4f", "dcw5f", False),
            ("DOG", "dog", False),
            ("dog ", "dog", False),
            ("aaab", "bbba", False),
        )
    def test_cp(self):
        for str1,str2,expected in self.test_cases1:
            assert checkPerm(str1, str2) == expected 
            print("this is the problem:",str1,str2)
         # true check
        

if __name__ == "__main__":
    unittest.main()
###