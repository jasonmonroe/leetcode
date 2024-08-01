<?php

/*
|--------------------------------------------------------------------------
| Counting Sort #1
|--------------------------------------------------------------------------
| HankerRank
| @link https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/copy-from/384024965
|
| Complete the 'countingSort' function below.
|
| The function is expected to return an INTEGER_ARRAY.
| The function accepts INTEGER_ARRAY arr as parameter.
|
| Input:
| 100 63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94
| 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95
| 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33
|
| Expected Output:
| 0 2 0 2 0 0 1 0 1 2 1 0 1 1 0 0 2 0 1 0 1 2 1 1 1 3 0 2 0 0 2 0 3 3 1 0 0 0 0 2 2 1 1 1 2 0 2 0 1 0 1 0 0 1 0 0 2 1 0
| 1 1 1 0 1 0 1 0 2 1 3 2 0 0 2 1 2 1 0 2 2 1 2 1 2 1 1 2 2 0 3 2 1 1 0 1 1 1 0 2 2
|
*/

function countingSort(array $arr): array
{
    // Write your code here
    $MIN = 100;
    $MAX = pow(10, 6);
    $cnt = count($arr);

    if ($cnt < $MIN || $cnt > $MAX) {
        return [];
    }

    $arrValCnts = initArrayValueCnts($cnt);

    // tally values
    for ($i=0; $i<$cnt; $i++) {
        $val = $arr[$i];

        if ($val >= 0 && $val < 100) {
            $arrValCnts[$val]++;
        }
    }

    return array_slice($arrValCnts, 0, 100);
}

function initArrayValueCnts(int $cnt) : array
{
    $arrValCnts = [];
    for ($i=0; $i<$cnt; $i++) {
        $arrValCnts[$i] = 0;
    }

    return $arrValCnts;
}

// Start here...
$fptr = fopen(getenv("OUTPUT_PATH"), "w");
$n = intval(trim(fgets(STDIN)));
$arr_temp = rtrim(fgets(STDIN));

$arr = array_map('intval', preg_split('/ /', $arr_temp, -1, PREG_SPLIT_NO_EMPTY));
$result = countingSort($arr);

fwrite($fptr, implode(" ", $result) . "\n");

fclose($fptr);
