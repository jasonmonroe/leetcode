<?php
/*
|--------------------------------------------------------------------------
| Merge k Sorted Lists
|--------------------------------------------------------------------------
| #23
| Description
| You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
|
| Merge all the linked-lists into one sorted linked-list and return it.
|
| Example 1:
|
| Input: lists = [[1,4,5],[1,3,4],[2,6]]
| Output: [1,1,2,3,4,4,5,6]
| Explanation: The linked-lists are:
| [
|   1->4->5,
|   1->3->4,
|   2->6
| ]
| merging them into one sorted list:
| 1->1->2->3->4->4->5->6
| Example 2:
|
| Input: lists = []
| Output: []
| Example 3:
|
| Input: lists = [[]]
| Output: []
|
| @link https://leetcode.com/problems/merge-k-sorted-lists/description/
| @link https://leetcode.com/problems/merge-k-sorted-lists/submissions/1475615254/
|
*/

// Definition for a singly-linked list.
class ListNode {
    protected int $val;
    public mixed $next;

    public function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }

    /**
     * @return int
     */
    public function getValue() : int
    {
        return $this->val;
    }
}


class Solution {
    
    /**
     * @param array $lists
     * @return ListNode|null
     */
    function mergeKLists(array $lists): ?ListNode
    {
        $len = count($lists);

        // Constraints
        if ($len <= 0 || $len > pow(10, 4)) {
            return null;
        }

        // Build single node with sorted values.
        $firstNode = null;
        $sortedList = null;

        // Build link lists based on sorted array.
        $values = $this->getSortedValues($lists);
        sort($values);

        for ($i = 0; $i < count($values); $i++) {
            $value = $values[$i];

            if ($value === null || $value === '') {
                continue;
            }

            $newNode = new ListNode($value);

            // Check for head.
            if ($firstNode === null) {
                $firstNode = $newNode;
                $sortedList = $firstNode;
                continue;
            }

            $currNode = $firstNode;

            // Moving pointer.
            while ($currNode->next !== null) {
                $currNode = $currNode->next;
            }

            $currNode->next = $newNode;
        }

        return $sortedList;
    }
    
    /**
     * Add linked list values to array then sort them.
     *
     * @param array $lists
     * @return array
     */
    function getSortedValues(array $lists): array
    {
        $values = [];
        for ($i = 0; $i < count($lists); $i++) {
            $node = $lists[$i];
            $j = count($values);
            
            while ($node->next !== null) {
                $values[$j] = $node->getValue();
                $j++;

                $node = $node->next;
            }

            // Add last value to array.
            $values[$j] = $node->getValue();
        }

        return $values;
    }
}
