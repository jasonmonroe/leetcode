<?php

/*
|--------------------------------------------------------------------------
| Minimum Window Substring
|--------------------------------------------------------------------------
| #76
| Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every
| character in t (including duplicates) is included in the window. If there is no such substring, return the empty
| string "".
|
| The testcases will be generated such that the answer is unique.
|
| @link https://leetcode.com/problems/minimum-window-substring/
|
*/
class Solution {

    /**
     * @param string $s
     * @param string $t
     * @return string
     */
    public function minWindow(string $s, string $t) : string
    {
        // hastack len, needle lens
        $haystack = '';
        $m = strlen($s);
        $n = strlen($t);

        // constraints
        if ($m < 1 || $n > pow(10, 5)) {
            return '';
        }

        if ($n > $m) {
            return $haystack;
        }

        // Return minimum substring of $s that has at least all the chars of $t any additional chars are acceptable as
        // long as they're continuous.
        $offset = 0;
        $haystackLen = $n;

        do {
            $haystack = substr($s, $offset, $haystackLen);

            // Increment haystack len after exhausting options.
            $chkHaystackLen = ($m - $haystackLen);

            if ($offset === $chkHaystackLen) {
                $offset = 0;
                $haystackLen++;
            } else {
                $offset++;
            }
        } while (!$this->chkHaystack($haystack, $t, $n));

        return $haystack;
    }

    /**
     * Check if str (haystack) has all chars of t.
     *
     * @param string $haystack
     * @param string $t
     * @param int $n
     * @return bool
     */
    protected function chkHaystack(string $haystack, string $t, int $n): bool
    {
        for ($k = 0; $k < $n; $k++) {
            $needle = $t[$k];
            if (!str_contains($haystack, $needle)) {
                return false;
            }

            if (!$this->cmpNeedles($haystack, $needle, $t)) {
                return false;
            }
        }

        // Now that we have all needles found in haystack check if the len is greater or equal to the len of $t.
        return strlen($haystack) >= $n;
    }

    /**
     * Does the count === count in t
     *
     * @param string $haystack
     * @param string $needle
     * @param string $t
     * @return bool
     */
    protected function cmpNeedles(string $haystack, string $needle, string $t): bool
    {
        return substr_count($t, $needle) <= substr_count($haystack, $needle);
    }
}

// Sample Inputs
$s = 'ADOBECODEBANC';
$t = 'ABC';
$ans = 'BANC';

$obj = new Solution();
$output = $obj->minWindow($s, $t);

print_r([
    's' => $s,
    't' => $t,
    'output' => $output
]);

if ($output === $ans) {
    echo "Your output ($output) is correct!\n";
}
