"""
--------------------------------------------------------------------------
Reverse Words in a String
--------------------------------------------------------------------------
LeetCode #151
Link: https://leetcode.com/problems/reverse-words-in-a-string/submissions/1478932802/

Problem Statement:
Given an input string `s`, reverse the order of the words.

- A word is defined as a sequence of non-space characters.
- The words in `s` will be separated by at least one space.
- The returned string should have the words in reverse order, concatenated by a single space.
- `s` may contain leading or trailing spaces, or multiple spaces between words.
- The output should not contain extra spaces—only a single space should separate words.

Example:
    Input: "  hello   world  "
    Output: "world hello"
"""

class Solution:
    def reverse_words(self, s: str):
        # Add constraints.
        if len(s) == 0 or len(s) > pow(10, 4):
            return None

        # Remove extra space!
        s = ' '.join(s.split())
        words = s.split(' ')
        flipped = words[::-1]
        output = ' '.join(flipped)

        return output
