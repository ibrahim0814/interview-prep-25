# https://neetcode.io/problems/two-integer-sum?list=blind75

"""
Two Sum
Solved 
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force - double for loop, for every number compare it to all other numbers in the array
        # map approach
        # need 4 at index 0
        # first pass we do compliment -> index
        # second pass 
            # do we have 4? yes! where? at index 1
            # take current index
            # take compliment index
            # put in array and then output
        

        ci = {}

        for i in range(len(nums)):
            num = nums[i]
            if num not in ci:
                ci[num] = i
        
        for i in range(len(nums)):
            compliment = target - nums[i]
            # REVIEW: trouble here because the numbers can be the same but index needs to differ
            if compliment in ci and i != ci[compliment]:
                index1 = ci[compliment]
                index2 = i
                # REVIEW: trouble here because i wanted to return a sorted array
                ret = sorted([index1, index2])
                return ret
