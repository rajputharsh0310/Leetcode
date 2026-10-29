class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        length=1
        max_length=1
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                length+=1
                max_length=max(length,max_length)
            elif nums[i]==nums[i-1]:
                continue
            else:
                length=1
        return max_length

        