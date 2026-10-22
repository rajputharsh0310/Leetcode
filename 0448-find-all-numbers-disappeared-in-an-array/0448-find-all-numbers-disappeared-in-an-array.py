class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def cycle_sort(nums):
            n=len(nums)
            i=0
            while i<n:
                correct_index=nums[i]-1
                if nums[i]!=nums[correct_index]:
                    nums[i],nums[correct_index]=nums[correct_index],nums[i]
                else:
                    i+=1
            return nums
        cycle_sort(nums)
        missing=[]
        for i, num in enumerate(nums):
            if num!=i+1:
                missing.append(i+1)
        return missing
        