class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max=max_sum=nums[0]
        current_min=min_sum=nums[0]
        for i in range(1,len(nums)):
            current_max=max(nums[i],current_max+nums[i])
            max_sum=max(current_max,max_sum)
            current_min=min(nums[i],current_min+nums[i])
            min_sum=min(current_min,min_sum)
        return max(abs(max_sum),abs(min_sum))