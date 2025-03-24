LeetCode Solutions

📌 About

This repository contains my solutions to various LeetCode problems, categorized by difficulty and topic. The goal is to improve problem-solving skills and prepare for coding interviews, especially for FAANG companies.

🚀 Table of Contents
•	Problem Categories
•	Solution Format
•	Progress Tracking
•	How to Use
•	Resources

📂 Problem Categories

The solutions are organized into the following categories:

🟢 Easy
•	Two Sum
•	Merge Two Sorted Lists
•	Palindrome
•	Power of Two
•	Search Insert Position
•	Valid Palindrome II

🟠 Medium
•	Container With Most Water
•	Count Primes
•	Random Pick Index
•	Reverse Words In A String
•	Single Number III
•	Top K Frequent Elements
•	

🔴 Hard
•	Median of Two Sorted Arrays
•	Merge K Sorted List
•	Minimum Window Substring
•	Trapping Rain Water

🛠️ Solution Format

Each solution follows a structured format:
•	Problem Name: Linked to the problem on LeetCode
•	Difficulty: Easy / Medium / Hard
•	Solution: Python / JavaScript / Java (Multiple implementations if applicable)
•	Explanation: Step-by-step breakdown of the approach
•	Time & Space Complexity: Analyzed for efficiency

Example:

# Problem: Two Sum (Easy)
# https://leetcode.com/problems/two-sum/

def two_sum(nums, target):
hashmap = {}
for i, num in enumerate(nums):
diff = target - num
if diff in hashmap:
return [hashmap[diff], i]
hashmap[num] = i
return []

✅ Progress Tracking

Use this table to track solved problems:

#	Problem	Difficulty	Solution	Notes
1	Two Sum	🟢 Easy	Python	Hashmap approach
2	Add Two Numbers	🟠 Medium	Java	Linked List manipulation

🔍 How to Use
1.	Clone the repository:

git clone https://github.com/jasonmonroe/leetcode.git
cd leetcode

	2.	Browse problems in the /solutions folder.
	3.	Run a solution:

python solutions/two_sum.py

	4.	Contribute new solutions by creating a pull request.

📚 Resources
•	LeetCode
•	NeetCode
•	GeeksforGeeks

⸻

Happy Coding! 🚀