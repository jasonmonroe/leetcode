<?php

/*
|--------------------------------------------------------------------------
| Container With Most Water
|--------------------------------------------------------------------------
| #11
| You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
| the ith line are (i, 0) and (i, height[i]).
|
| Find two lines that together with the x-axis form a container, such that the container contains the most water.
| Return the maximum amount of water a container can store.
|
| Notice that you may not slant the container.
|
| @link https://leetcode.com/problems/container-with-most-water/description/
|
*/
class Solution {

    /**
     * Gets the max area of water in the container from all the height values in the array.
     *
     * @param array $height
     * @return int
     */
    public function maxArea(array $height) : int
    {
        $n = count($height);
        $maxArea = 0;
        $minHeightCnt = 2;
        $maxHeightCnt = pow(10, 5);

        // If out of range return.
        if ($n < $minHeightCnt || $n > $maxHeightCnt) {
            return 0;
        }

        // Find the new lines that will contain the most water meaning they're the highest?
        // area = width * height
        // For every height value, calculate width (distance) and height of the value to determine area.
        // If array is over 20,000 start from the middle and calc backwards and multiply by 2 when values repeat.
        if ($n >= 20000) {
            $maxArea = $this->calcHeightCntGt20000($n, $height);
        } else {
            for ($i = 0; $i < $n; $i++) {
                for ($j = 0; $j < $n; $j++) {
                    if ($this->chkHeightValRange($height, $i, $j)) {
                        continue;
                    }

                    // Get max area of container.
                    $maxArea = $this->getMaxArea($this->calcArea($height, $i, $j), $maxArea);
                }
            }
        }

        return $maxArea;
    }

    /**
     * Calculate area. Calculate width by subtracting left and right indexes. Calculate height by getting the min
     * value of each side since the min value is what actually holds the water in the container.
     *
     * @param array $height
     * @param int $i
     * @param int $j
     * @return int
     */
    public function calcArea(array $height, int $i, int $j) : int
    {
        $w = abs($j - $i);
        $h = min($height[$i], $height[$j]);

        return $w * $h;
    }

    /**
     * Get max area of all possible heights.
     *
     * @param int $area
     * @param int $maxArea
     * @return int
     */
    public function getMaxArea(int $area, int $maxArea) : int
    {
        return max($area, $maxArea);
    }

    /**
     * Check if height values are out of range.
     *
     * @param int $heightVal
     * @return bool
     */

    /**
     * Checks if the values in the height array are within the min and max constraints.
     * Note: Also returns true if increments i and j are the same.
     *
     * @param array $heightArr
     * @param int $i
     * @param int $j
     * @return bool
     */
    public function chkHeightValRange(array $heightArr, int $i, int $j) : bool
    {
        $maxVal = pow(10, 4);
        return $i === $j ||
            (
                ($heightArr[$i] < 1 || $heightArr[$i] > $maxVal) || ($heightArr[$j] < 1 || $heightArr[$j] > $maxVal)
            );
    }

    public function chkHeightValRange2(int $heightVal) : bool
    {
        return $heightVal < 1 || $heightVal > pow(10, 4);
    }

    /**
     * @param int $n
     * @param array $height
     * @return float|int
     */
    public function calcHeightCntGt20000(int $n, array $height): float|int
    {
        $maxArea = 0;
        for ($i = $n/2; $i > 0; $i--) {
            for ($j = 0; $j< $n/2; $j++) {
                if ($this->chkHeightValRange($height, $i, $j)) {
                    continue;
                }
                $newMaxArea = $this->getMaxArea($this->calcArea($height, $i, $j), $maxArea);
                if ($newMaxArea === $maxArea) {

                    return $newMaxArea * 2;
                } else {
                    $maxArea = $newMaxArea;
                }
            }
        }

        return $maxArea;
    }

    /**
     * Initialize height array
     * @return int[]
     */
    public function getHeight() : array
    {
        $height = [];
        if (mt_rand(0,1) === 0) {
            $height = [1,8,6,2,5,4,8,3,7];
        } else {
            $randNo = mt_rand(4, 1000);
            for ($i=0; $i<$randNo; $i++){
                $height[] = mt_rand(1, 100);
            }
            shuffle($height);
            $height = array_values($height);
        }

        return $height;
    }
}

/**
 * Input: height = [1,8,6,2,5,4,8,3,7]
 * Output: 49
 * Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of
 * water (blue section) the container can contain is 49.
 */
$obj = new Solution();
$height = $obj->getHeight();
$output = $obj->maxArea($height);

print_r([
    'height' => $height,
    'output' => $output,
]);
