"""
Group Anagrams
Solved 
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # i go through each word
        # then i 

        mapToWordsArr = {}
        for word in strs:
            charArr = [0] * 26 
            for char in word:
                index = ord(char) - ord('a')
                #print(index)
                charArr[index] = charArr[index] + 1
                print(charArr[index])
            combinedString = ''
            for idx in range(len(charArr)):
                num = charArr[idx]
                charValue = ord('a') + idx
                actualChar = chr(charValue)
                combinedString = "{c}{a}{n}".format(c=combinedString, a=actualChar,n=num)
            print(combinedString)
            if combinedString not in mapToWordsArr:
                mapToWordsArr[combinedString] = [word]
            else:
                currMappedArr = mapToWordsArr[combinedString]
                currMappedArr.append(word)
        
        finalArr = []
        for values in mapToWordsArr.values():
            finalArr.append(values)
        
        return finalArr
            


        