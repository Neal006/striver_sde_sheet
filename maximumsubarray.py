from ast import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local = 0
        glob = float('-inf')
        for i in range(len(nums)):
            cN = nums[i]
            local = max(local + cN, cN)
            glob = max(glob, local)
        return glob