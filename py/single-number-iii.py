###
#--------------------------------------------------------------------------
# Single Number III
#--------------------------------------------------------------------------
# #260
# @link https://leetcode.com/problems/single-number-iii/submissions/1478775806/
#
# Given an integer array nums, in which exactly two elements appear only once
# and all the other elements appear exactly twice. Find the two elements that
# appear only once. You can return the answer in any order.
#
###

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        output = []
        for i in range (len(nums)):
            if nums.count(nums[i]) == 1:
                output.append(nums[i])

        return output
