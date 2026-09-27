class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        count=0
        h={}
        for right in range(len(nums)):
            h[nums[right]]=h.get(nums[right],0)+1
            while h.get(0,0)>1:
                h[nums[left]]-=1
                left+=1
            count=max(count,right-left)
        return count
