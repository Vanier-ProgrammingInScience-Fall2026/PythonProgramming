# Programming in Science – Lab 6-List

### Question(s)

1. Write a function `count_num(nums, target)` that receives a list of numbers, and a target number, then count the number of appearances of the target in the list.

#### Example:
- [1,2,3,1,2,3], 2 -> 2
- [1,1,1,1,2,3], 1 -> 4
- [1,2,3,4,5], 6 -> 0

2. Write a function `find_shared_num(nums1, nums2)` that receives two lists 
   of numbers and returns all numbers that appear in both two lists.

#### Example:
- [1,2,3], [3,4,5] -> [3]
- [1,2,3,4], [4, 2] -> [2, 4]
- [1,2,3], [4,5,6] -> []  

3. Write a function `remove_element(nums, threshold)` that receives a list of numbers, and a threshold, the function returns a new list that contains the number bigger than the threshold in the input list.

#### Example:
- [95, 74, 80, 62], 75 -> [95, 80]
- [95, 74, 80, 62], 98 -> []
- [95, 74, 80, 62], 60 -> [95, 74, 80, 62]

4. Write a function `update_nums(nums)` that takes a list of numbers, 
   increase each number at even position by 1, and decrease each number at odd position by 1, return the results in a new list.

#### Example (n = 4):
- [1, 2, 3, 4] -> [2, 1, 4, 3]
- [4, 1, 6, 4] -> [5, 0, 7, 3]
