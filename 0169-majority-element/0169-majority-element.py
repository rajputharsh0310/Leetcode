class Solution(object):
    def majorityElement(self, nums):
        count={}
        for i, num in enumerate(nums):
            count[num]=count.get(num,0)+1
        for num in count:
            if count[num]>len(nums)//2:
                return num
            