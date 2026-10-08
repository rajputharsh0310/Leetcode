class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count={0:-1}
        prefix=0
        for i, num in enumerate(nums):
            prefix+=num
            remainder=prefix%k
            if remainder in count:
                if i-count[remainder]>=2:
                    return True
            else:
                count[remainder]=i
        return False
        