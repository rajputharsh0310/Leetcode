class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash1={}
        for num in nums1:
            hash1[num]=hash1.get(num,0)+1
        hash2={}
        for num in nums2:
            hash2[num]=hash2.get(num,0)+1
        result=[]
        for num in hash1:
            if num in hash2:
                count=min(hash1[num],hash2[num])
                result.extend([num]*count)
        return result