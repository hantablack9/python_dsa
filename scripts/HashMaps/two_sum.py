# https://leetcode.com/problems/two-sum/solutions/6996384/best-performing-two-sum-in-on-time-space-hoiq

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Returns: Indices of the pair that sum up to the target
        """
        # Using dictionary for O(1) time lookup
        map_ = {} # Dict to map the idx i of num[i] to its index (they are a two-sum pair)

        if all(-10**9 <= num <= 10**9 for num in nums):
            if 2<=len(nums)<=10**4 and -10**9<= target <=10**9:
                for pos_i, num in enumerate(nums):
                    complement = target -  num
                    if complement in map_:
                        return [pos_i, map_[complement]]
                    map_[num] = pos_i        
        return []