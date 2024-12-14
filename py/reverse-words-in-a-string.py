###
#--------------------------------------------------------------------------
# Reverse Words in a String
#--------------------------------------------------------------------------
# #151
# @link https://leetcode.com/problems/reverse-words-in-a-string/submissions/1478932802/
#
# Given an input string s, reverse the order of the words.
#
# A word is defined as a sequence of non-space characters. The words in s will
# be separated by at least one space.
#
#  Return a string of the words in reverse order concatenated by a single space.
#
# Note that s may contain leading or trailing spaces or multiple spaces between
# two words. The returned string should only have a single space separating
# the words. Do not include any extra spaces.
#
###

class Solution:
    def reverseWords(self, s: str) -> str:
        # Add constraints.
        if (len(s) == 0 or len(s) > pow(10, 4)):
            return None

        # Remove extra space!
        s = ' '.join(s.split())
        words = s.split(' ')
        flipped = words[::-1]
        output = ' '.join(flipped)

        return output
