# https://neetcode.io/problems/is-anagram?list=blind75

"""
Valid Anagram
Solved 
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # construct a hashmap of letter -> occurances
        # do it for each string
        # also have a set of unique chars so we can compare letters after we run through them
        # use the same set for both
        # O(n) complexity where n is the length of the strings

        s_map = {}
        t_map = {}
        setChars = set()

        for char in s:
            if char in s_map:
                s_map[char] = s_map[char] + 1
            else:
                s_map[char] = 1
            setChars.add(char)
        
        for char in t:
            if char in t_map:
                t_map[char] = t_map[char] + 1
            else:
                t_map[char] = 1
            

        print(s_map, t_map)
        
        for char in setChars:
            print(char)
            if char in s_map and char in t_map:
                if s_map[char] != t_map[char]:
                    return False
            else:
                return False
        
        return True



        