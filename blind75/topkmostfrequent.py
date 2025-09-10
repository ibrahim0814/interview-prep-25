"""
Top K Frequent Elements
Solved 
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
Constraints:

1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap which maps number to tracker 
        # use a heap to continually keep track of top element, basically insert then sort
        
        # create hashmap with counts
        countsMap = {}
        for num in nums:
            if num in countsMap:
                countsMap[num] += 1
            else:
                countsMap[num] = 1
        
        # array of arrays this is going to map index which represents count to numbers which occur that many times
        freqArr = []

        # each array inside represents the collection of numbers which have that frequency at index
        for i in range(len(nums)+1):
            freqArr.append([])
        
        for num, freq in countsMap.items():
            freqArr[freq].append(num)
        
        numsStillNeeded = k
        answer = []
        
        # need to go backwards from the frequency array
        # number occured 6 times it'll be at index 5
        for i in range(len(freqArr) -1,0,-1):
            # depending on how many numbers we need we pop the k most frequent element
            # remmeber each mapping can have more than one number
            if len(freqArr[i]) > 0 and numsStillNeeded > 0:
                for num in freqArr[i]:
                    answer.append(num)
                    if numsStillNeeded > 0:
                        numsStillNeeded -= 1
                    else:
                        break
            else:
                continue
        
        return answer


        
        
        

        


