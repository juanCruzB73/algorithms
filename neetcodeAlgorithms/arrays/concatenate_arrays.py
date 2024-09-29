"""
Given an integer array nums of length n, you want to create an
array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
"""
class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        length=len(nums)
        ans=[]
        for i in range(2):
            for j in nums:
                ans.append(j)
        return ans
res=None
print(Solution.getConcatenation(res,[5,3,9,7]))