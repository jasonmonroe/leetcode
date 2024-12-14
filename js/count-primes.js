/*
|--------------------------------------------------------------------------
| Count Primes
|--------------------------------------------------------------------------
| #204
| Given an integer n, return the number of prime numbers that are strictly less than n.
|
| Example 1:
|
| Input: n = 10
| Output: 4
| Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
| Example 2:
|
| Input: n = 0
| Output: 0
| Example 3:
|
| Input: n = 1
| Output: 0
|
| @link https://leetcode.com/problems/count-primes/submissions/1478762537/
*/

/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {

    const nMax = 5 * Math.pow(10, 6)

    if (n <= 1 || n > nMax) {
        return 0
    }

    let primeCnt = 0
    let min = 2
    let max = n - 1
    let isPrime = true

    for (let i = max; i >= min; i--) {
        isPrime = true
        for (let j = min; j <= max; j++) {
            if (i === j) {
                continue
            }

            if (i % j === 0) {
                isPrime = false
            }
        }

        if (isPrime) {
            primeCnt++
        }
    }

    return primeCnt
};
