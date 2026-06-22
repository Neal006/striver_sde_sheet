from ast import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0,0,0]
        for i in range(len(nums)):
            count[nums[i]] += 1
        nums.clear()
        nums[0:count[0]] = [0]*count[0]
        nums[count[0]:count[0]+count[1]] = [1]*count[1]
        nums[count[0]+count[1]:count[0]+count[1]+count[2]] = [2]*count[2]