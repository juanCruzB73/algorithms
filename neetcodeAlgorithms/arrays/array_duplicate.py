"""
Given an integer array nums, return true if any value 
appears more than once in the array, otherwise return false.
"""
class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        hashet=set()
        for n in nums:
            if(n in hashet):
                return True
            hashet.add(n)
        return False
         