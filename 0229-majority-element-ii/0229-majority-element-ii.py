class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        candidate1=None
        candidate2=None
        count1=0
        count2=0
        for num in nums:
            if count1==0 and num!=candidate2:
                candidate1=num
            elif count2==0 and num!=candidate1:
                candidate2=num
            if num==candidate1:
                count1+=1
            elif num==candidate2:
                count2+=1
            else:
                count1-=1
                count2-=1
        n=len(nums)
        freq1=nums.count(candidate1)
        freq2=nums.count(candidate2)
        if freq1>n//3 and freq2>n//3 and candidate1!=candidate2:
            return [candidate1, candidate2]
        elif freq1>n//3:
            return [candidate1]
        elif freq2>n//3:
            return [candidate2]
        else:
            return []