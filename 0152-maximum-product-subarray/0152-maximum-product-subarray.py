class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_max=nums[0]
        current_min=nums[0]
        max_product=nums[0]
        for i in range(1,len(nums)):
            temp_max=current_max
            temp_min=current_min
            current_max=max(nums[i],temp_max*nums[i],temp_min*nums[i])
            current_min=min(nums[i],temp_max*nums[i],temp_min*nums[i])
            max_product=max(current_max,max_product)
        return max_product
        