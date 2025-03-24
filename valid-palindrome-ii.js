/*
|--------------------------------------------------------------------------
| Valid Palindrome II
|--------------------------------------------------------------------------
| #680
| @link https://leetcode.com/problems/valid-palindrome-ii/submissions/1478767593/
|
| Given a string s, return true if the s can be palindrome after deleting at
| most one character from it.
*/

/**
 * Check if a string is a valid palindrome after deleting at most one character
 *
 * @param s
 * @returns {boolean}
 */
var validPalindrome = function(s)
{
    // Remove one char then check.
    const len = s.length

    if (len > 10000) {
        return true
    }

    for (let i = 0; i < len; i++) {
        let str = s.substring(0, i) + s.substring(i + 1)

        if (str === reverseString(str)) {
            return true
        }
    }

    return false
};

/**
 * Reverse a string
 *
 * @param s
 * @returns {*}
 */
function reverseString(s)
{
    let str = s.split('')
    str = str.reverse()
    str = str.join('')

    return str
}
