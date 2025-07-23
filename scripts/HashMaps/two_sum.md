# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
The brute-force approach would take O(n^2) time. I figured I'd optimize for time by using a dict/hashmap for constant time lookups, and by trading O(n) space for linear time. Wy current solution beats 100% on time and 97% in space complexities.

# Approach
<!-- Describe your approach to solving the problem. -->
1. I initialized a mapper to map the number to its index, given its complement exists in the array nums.
2. I then used the outermost if...else block to check for the problem statements' constraints, to avoid scanning the imput list if not necessary and to return an empty list.
3. The socond if block is used to check for the remaining constraints.
4. The for loop is used to scan through the input list. This is set-up so that it immediately breaks and returns the solution if a complement is found.

# Complexity
- Time complexity: O(n)
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:O(n)
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python []
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Returns: Indices of the pair that sum up to the target
        """
        # Using dictionary for O(1) time lookup
        # Using search term and complement for scan in O(n) time 
        map_ = {} # Dict to map the idx i of num[i] to its COMPLEMENT (they are a two-sum pair)

        if all(-10**9 <= num <= 10**9 for num in nums):
            if 2<=len(nums)<=10**4 and -10**9<= target <=10**9:
                for pos_i, num in enumerate(nums):
                    complement = target -  num
                    if complement in map_:
                        return [pos_i, map_[complement]]
                    map_[num] = pos_i
        else:
            return []
```