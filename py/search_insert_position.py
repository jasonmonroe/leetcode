"""
--------------------------------------------------------------------------
Search Insert Position
--------------------------------------------------------------------------
LeetCode #35
Link: https://leetcode.com/problems/search-insert-position/submissions/1582615400

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity
"""

class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:

        index = -1
        if target in nums:
            return nums.index(target)

        elif target >= max(nums):
            return len(nums)

        elif target not in nums and len(nums) == 1:
            return 0

        else:
            i = 0
            for num in nums:
                if num > target:
                    return i
                else:
                    i += 1

        if index == -1:
            print("Error: Index not found!")

        return index
