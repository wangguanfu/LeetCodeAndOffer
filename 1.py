class Solution(object):
    """
       :type nums: List[int]
       :type target: int
       :rtype: List[int]
       """
    def twoSum(self, nums, target):
        tag = {}
        for i, v in enumerate(nums):
            if target - v in tag:
                return [nums[target - v], i]
            tag[nums] = i
