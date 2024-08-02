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
|    1->4->5,
|   1->3->4,
|  2->6
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
|
*/

// Definition for a singly-linked list.
class ListNode {
    public int $val = 0;
    public $next = null;

    function __construct($val = 0, $next = null) {
        $this->val = $val;
        $this->next = $next;
    }
}


class Solution {

    /**
     * @param ListNode[] $lists
     * @return ListNode|null
     */
    function mergeKLists($lists): ?ListNode
    {
        if (!$this->chkConstraints($lists)) {
            return;
        }

        $vals = $this->getOrderedValues($lists);

        // build single node with sorted values
        $firstNode = null;
        $currNode = null;

        // build link lists based on sorted array
        $size = count($vals);
        for ($i = 0; $i < $size; $i++) {

            if ($vals[$i] > 0) {
                $newNode = new ListNode($vals[$i]);

                // check for head
                if ($firstNode === null) {
                    $firstNode = $newNode;
                } else {
                    $currNode = $firstNode;

                    // Move pointer.
                    while ($currNode->next !== null) {
                        $currNode = $currNode->next;
                    }

                    $currNode->next = $newNode;
                }
            }

        }

        return $currNode;
    }

    /**
     * @param $lists
     * @return bool
     */
    function chkConstraints($lists): bool
    {
        $k = count($lists);

        if ($k <= 0 || $k > pow(10, 4)) {
            return false;
        }

        return true;
    }

    /**
     * @param $lists
     * @return array
     */
    function getOrderedValues($lists): array
    {
        $vals = [];

        for ($i=0, $j=0; $i<count($lists); $i++) {
            $node = $lists[$i];

            while ($node->val !== 0) {
                $vals[$j] = $node->val;
                $j++;

                // move ptr
                $node = $node->next;
            }
        }

        sort($vals);

        return $vals;
    }
}

// Run the test cases...
$tests = [
    [[1,4,5],[1,3,4],[2,6]],
    [],
    [[]]
];

$obj = new Solution();
$ans = $obj->mergeKLists($tests);

print_r($ans);
