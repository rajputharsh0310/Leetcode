class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=0
        count={0:-1}
        length=0
        max_length=0
        for i, num in enumerate(nums):
            if num==0:
                prefix-=1
            else:
                prefix+=1
            if prefix in count:
                length=i-count[prefix]
                max_length=max(length,max_length)
            else:
                count[prefix]=i
        return max_length
