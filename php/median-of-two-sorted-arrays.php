<?php

/*
|--------------------------------------------------------------------------
| Median of Two Sorted Arrays
|--------------------------------------------------------------------------
| #4
| Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
| The overall run time complexity should be O(log (m+n)).
|
| @link https://leetcode.com/problems/median-of-two-sorted-arrays/description/
|
*/

class Solution {

    /**
     * @param array $nums1
     * @param array $nums2
     * @return float
     */
    public function findMedianSortedArrays(array $nums1, array $nums2) : float
    {
        $m = count($nums1);
        $n = count($nums2);
        $o = $m + $n;

        // Set constraints.
        if ($m < 0 || $m > 1000 || $n < 0 || $n > 1000 || ($o < 0 || $o > 2000)) {
            return 0;
        }

        // clean nums
        $nums1 = $this->filter($nums1, $m);
        $nums2 = $this->filter($nums2, $n);

        // merge array
        $nums = array_merge($nums1, $nums2);

        // get median value of merged array
        return $this->getMedian($nums);
    }

    /**
     * Filter out values of nums that are beyond constraints.
     *
     * @param array $nums
     * @param int $cnt
     * @return array
     */
    protected function filter(array $nums, int $cnt): array
    {
        $maxValue = pow(10, 6);

        for ($i = 0; $i < $cnt; $i++) {
            if ($nums[$i] < (-1 * $maxValue) || $nums[$i] > $maxValue) {
                unset($nums[$i]);
            }
        }

        return $nums;
    }

    /**
     * Get median value.
     *
     * @param array $nums
     * @return float|int|mixed
     */
    protected function getMedian(array $nums): mixed
    {
        $cnt = count($nums);
        sort($nums);

        if ($cnt % 2 === 0) {
            $medianIndex = $cnt / 2;
            return ($nums[$medianIndex-1] + $nums[$medianIndex]) / 2;
        } else {
            $medianIndex = floor($cnt / 2);
            return $nums[$medianIndex];
        }
    }
}

/*
Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
*/

// Define num #1.
$nums1 = [];
$randNo = mt_rand(2, 20);
for ($i = 0; $i < $randNo; $i++) {
    $nums1[$i] = mt_rand(1, 50);
}
$nums1 = array_unique($nums1);
ksort($nums1);

// Define num #2.
$nums2 = [];
$randNo = mt_rand(1, 20);
for ($i = 0; $i < $randNo; $i++) {
    $nums2[$i] = mt_rand(1, 50);
}
$nums2 = array_unique($nums2);
ksort($nums2);

$obj = new Solution();
$output = $obj->findMedianSortedArrays($nums1, $nums2);

print_r([
    'nums1' => $nums1,
    'nums2' => $nums2,
    'output' => $output,
]);
