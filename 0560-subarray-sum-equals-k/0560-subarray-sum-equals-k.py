class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count={0:1}
        prefix=0
        ans=0
        for num in nums:
            prefix+=num
            required=prefix-k
            if required in count:
                ans+=count[required]
            count[prefix]=count.get(prefix,0)+1
        return ans