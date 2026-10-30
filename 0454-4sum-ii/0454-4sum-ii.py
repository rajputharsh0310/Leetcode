class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        hash={}
        for a in nums1:
            for b in nums2:
                hash[a+b]=hash.get(a+b,0)+1
        count=0
        for c in nums3:
            for d in nums4:
                target=-(c+d)
                count+=hash.get(target,0)
        return count