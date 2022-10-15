"""
76. Minimum Window Substring
Hard
12.4K
571
Companies
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string."""

"brute force"
def minWindow(s,t):
    allSubs=[]
    ans=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            allSubs.append(s[i:j])
    for elem in allSubs:
        # print("elem:",elem)
        toggle = True
        temp = elem
        for k in range(len(t)):
            if len(elem)< len(t) or t[k] not in temp:
                toggle = False
            else:
                # print("t[k]",t[k])
                # print("temp:",temp)
                removeIndex = temp.index((t[k]))
                print("removeIndex: ",removeIndex)
                temp= temp[0 : removeIndex : ] + temp[removeIndex + 1 : :]
                print("new temp:",temp)
                
        if toggle is True:
            ans.append(elem)
        else:
            toggle = True
        
        ans.sort(key=len)# sort based on the length
    return ans[0] if len(ans) != 0 else '""'



# print(minWindow("abca","bc"))
# print(minWindow("bbaa","aba"))

def minWindowSlide(s,t):
    arr = []
    word=""
    temp = t
    startArr=[]

    # for i in range(len(s)):
    i=0
    while i < len(s):
        if s[i] in temp or s[i] in t:
            startArr.append(i) #put the letter in the array of starting points
            if s[i] in temp:
                removeIndex = temp.index(s[i])
                # then remove that letter from the temp
                temp= temp[0 : removeIndex : ] + temp[removeIndex + 1 : :]
            i += 1
        else:
            i += 1
        if len(temp) == 0:
            #lets build the word
            print("sartArray 1: ",startArr)
            
            word = s[startArr.pop(0):i]
            print("word: ",word)
            i=startArr[0]
            
            # print("sartArray 2 after pop: ",startArr)
            # print("word: ",word)
            arr.append(word)
            word = ""
            temp = t
    arr.sort(key=len)
    return arr[0] if len(arr) !=0 else "''"


# print(minWindowSlide("xyzaeckbldabec","abc"))
print(minWindowSlide("bbaa","aba"))
print(minWindowSlide("bklbaa","aba"))
print(minWindowSlide("ADOBECODEBANC","ABC"))

S = "wegdtzwabazduwwdysdetrrctotpcepalxdewzezbfewbabbseinxbqqplitpxtcwwhuyntbtzxwzyaufihclztckdwccpeyonumbpnuonsnnsjscrvpsqsftohvfnvtbphcgxyumqjzltspmphefzjypsvugqqjhzlnylhkdqmolggxvneaopadivzqnpzurmhpxqcaiqruwztroxtcnvhxqgndyozpcigzykbiaucyvwrjvknifufxducbkbsmlanllpunlyohwfsssiazeixhebipfcdqdrcqiwftutcrbxjthlulvttcvdtaiwqlnsdvqkrngvghupcbcwnaqiclnvnvtfihylcqwvderjllannflchdklqxidvbjdijrnbpkftbqgpttcagghkqucpcgmfrqqajdbynitrbzgwukyaqhmibpzfxmkoeaqnftnvegohfudbgbbyiqglhhqevcszdkokdbhjjvqqrvrxyvvgldtuljygmsircydhalrlgjeyfvxdstmfyhzjrxsfpcytabdcmwqvhuvmpssingpmnpvgmpletjzunewbamwiirwymqizwxlmojsbaehupiocnmenbcxjwujimthjtvvhenkettylcoppdveeycpuybekulvpgqzmgjrbdrmficwlxarxegrejvrejmvrfuenexojqdqyfmjeoacvjvzsrqycfuvmozzuypfpsvnzjxeazgvibubunzyuvugmvhguyojrlysvxwxxesfioiebidxdzfpumyon"
T = "ozgzyywxvtublcl"
print(minWindowSlide(S,T))