/*
|--------------------------------------------------------------------------
| Top K Frequent Elements
|--------------------------------------------------------------------------
| #347
| Given an integer array nums and an integer k, return the k most frequent
| elements. You may return the answer in any order.
|
| @link https://leetcode.com/problems/top-k-frequent-elements/submissions/1472322169/
|
*/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
let topKFrequent = function(nums, k) {
    console.log('nums',nums,'k',k)
    const n = nums
    const len = n.length

    // constraints
    if (len < 1 && len > Math.pow(10, 5)) {
        return
    }

    for (let i = 0; i < len; i++) {
        if (len[i] < Math.pow(-10, 4) || len[i] > Math.pow(10, 4)) {
            return
        }
    }

    if (k < 1 ) {
        return
    }

    // Get unique numbers
    const uniques = n.filter((value, index, self) => {
        return self.indexOf(value) === index;
    });

    // Foreach unique number count how many are in the array.
    const uniqueCnts = []
    let map = new Map()
    for (let i = 0; i < uniques.length; i++) {
        let key = uniques[i]
        let cnt = 0
        for (let j = 0; j < len; j++) {
            if (n[j] === key) {
                cnt++
            }
        }

        map.set(key.toString(), cnt)
    }

    const mapArray = Array.from(map);
    let sorted = mapArray.sort((a, b) => b[1] - a[1]);

    // Return the top k items
    let output = []
    for (let i = 0; i < k; i++) {
        let arr = sorted[i]
        output.push(parseInt(arr[0], 10))
    }

    return output
};
