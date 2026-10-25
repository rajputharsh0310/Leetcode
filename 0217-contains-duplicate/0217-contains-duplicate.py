class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash={}
        for num in nums:
            hash[num]=hash.get(num,0)+1
        
        for num in hash:
            if hash[num]>1:
                return True
        return False