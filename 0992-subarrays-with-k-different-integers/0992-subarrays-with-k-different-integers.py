class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def most(k):
            left=0
            count=0
            h={}
            for right in range(len(nums)):
                h[nums[right]]=h.get(nums[right],0)+1
                while len(h)>k:
                    old=nums[left]
                    h[old]-=1
                    if h[old]==0:
                        del h[old]
                    left+=1
                count+=right-left+1
            return count
        return most(k)-most(k-1) 