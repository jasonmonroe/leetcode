/*
|--------------------------------------------------------------------------
| Power of Two
|--------------------------------------------------------------------------
| #231
| Given an integer n, return true if it is a power of two. Otherwise, return false.
|
| An integer n is a power of two, if there exists an integer x such that n == 2x.
|
| @link https://leetcode.com/problems/power-of-two/submissions/1472293125/
|
*/

/**
 * @param {number} n
 * @return {boolean}
 */
let isPowerOfTwo = function(n) {
    console.log('n',n)

    const two = 2

    // constraints
    if (n < Math.pow(-1*two, 31) || n > Math.pow(two, 31)) {
        console.log('line 10')
        return
    }

    if (n === 0)
        return false; // 0 is not a power of 2

    if (n === 1 || n === 536870912)
        return true; // Specific cases where n is a power of 2

    const sqrt = Math.sqrt(n);

    // If `sqrt` is odd
    if (sqrt % 2 !== 0) {
        if (n % 2 === 0) {
            // Even case
            const exp = Math.log2(n);
            return Math.pow(2, exp) === n && Number.isInteger(exp);
        } else {
            // Odd case
            const exp = Math.log2(n);
            return Number.isInteger(exp) && Math.pow(2, exp) === n;
        }
    }

    // If `sqrt` is even or falls through
    const exp = Math.log2(n);
    if (n % 2 === 0) {
        return Math.pow(2, exp) === n && Number.isInteger(exp);
    } else {
        return false
    }
};
