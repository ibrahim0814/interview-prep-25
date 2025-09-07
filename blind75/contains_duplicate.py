# https://neetcode.io/problems/duplicate-integer?list=blind75

"""
Contains Duplicate
Solved 
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

"""

from ast import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # using a set
        my_hashmap = set()
        for num in nums:
            if num in my_hashmap:
                return True
            else:
                my_hashmap.add(num)
        return False
        