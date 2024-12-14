###
#--------------------------------------------------------------------------
# Random Pick Index
#--------------------------------------------------------------------------
# #398
# @link https://leetcode.com/problems/random-pick-index/submissions/1478187374/
#
# Given an integer array nums with possible duplicates, randomly output the
# index of a given target number. You can assume that the given target number
# must exist in the array.
#
# Implement the Solution class:
#
# Solution(int[] nums) Initializes the object with the array nums.
# int pick(int target) Picks a random index i from nums where nums[i] == target.
# If there are multiple valid i's, then each index should have an equal
# probability of returning.
#
###
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(self.nums)

    def pick(self, target: int) -> int:
        max = 2 * pow(10, 4)

        # If array size exceeds max exit.
        if self.length < 0 or self.length > max:
            return None

        count = self.nums.count(target)

        if (count == 0):
            index = None

        elif (count == 1):
            index = self.nums.index(target)

        elif (count >= 19000):
            index = self.get_random_index(target)

        else:
            index = self.get_target_index(target)

        return index

    def get_target_index(self, target):
        indices = []
        for i in range (0, self.length):
            if target == self.nums[i]:
                indices.append(i)

        return indices[random.randint(0, len(indices) - 1)]

    def rno(self):
        return random.randint(0, self.length - 1)

    # Special case for 20,000+ indices.  Count indices that are NOT target.
    def get_random_index(self, target):
        # There are approx. 100 index values out of 20,000 that are not a match.
        rand_no = self.rno()

        # If random index value is not the target, pick a new random index value until found.
        while target != self.nums[rand_no]:
            rand_no = self.rno()

        return rand_no


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
