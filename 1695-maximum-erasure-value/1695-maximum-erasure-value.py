class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        count=0
        max_count=0
        seen=set()
        for right in range(len(nums)):
            while nums[right] in seen:
                count-=nums[left]
                seen.remove(nums[left])
                left+=1
            seen.add(nums[right])
            count+=nums[right]
            max_count=max(max_count,count)
        return max_count