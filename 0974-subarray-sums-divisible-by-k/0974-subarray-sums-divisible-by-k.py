class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count={0:1}
        ans=0
        prefix=0
        for num in nums:
            prefix+=num
            remainder=prefix%k
            if remainder in count:
                ans+=count[remainder]
            count[remainder]=count.get(remainder,0)+1
        return ans
        