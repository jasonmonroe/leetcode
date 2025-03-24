"""
|--------------------------------------------------------------------------
| Trapping Rain Water
|--------------------------------------------------------------------------
| #42
| @link https://leetcode.com/problems/trapping-rain-water/submissions/1542125415/
| Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water 
| it can trap after raining.
|
| Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
| Output: 6
| Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 
| 6 units of rainwater (blue section) are being trapped.
|
| Example 2:
| Input: height = [4,2,0,3,2,5]
| Output: 9
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """

        :param height:
        :return: water_sum: int
        """
        water_sum = 0
        curr = 1

        for curr_pos in range(curr, len(height) - 1):
            curr_height = height[curr_pos]

            # Get minimum border height
            min_height = min(max(height[:curr_pos]), max(height[curr_pos:]))
            water_diff = abs(curr_height - min_height)

            # Check conditions
            if curr_height == min(curr_height, min_height) and water_diff > 0:
                water_sum += water_diff

        return water_sum
