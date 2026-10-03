class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=[0]
        for num in nums:
            prefix.append(prefix[-1]+num)
        
        for i in range(len(prefix)):
            if i>0 and (prefix[-1]-prefix[i])==prefix[i-1]:
                return i-1
        return -1