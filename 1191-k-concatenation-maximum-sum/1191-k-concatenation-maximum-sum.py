class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        MOD=10**9 + 7
        current_max=arr[0]
        max_sum=arr[0]
        for i in range(1,len(arr)):
            current_max=max(arr[i],current_max+arr[i])
            max_sum=max(max_sum,current_max)
        
        total=sum(arr)
        prefix=0
        max_prefix=float('-inf')
        for num in arr:
            prefix+=num
            max_prefix=max(prefix,max_prefix)
        suffix=0
        max_suffix=float('-inf')
        for num in reversed(arr):
            suffix+=num
            max_suffix=max(max_suffix,suffix)
        if k==1:
            return max(0,max_sum)%MOD
        crossing_sum=max_prefix+max_suffix
        if total>0:
            crossing_sum+=(k-2)*total
        return max(0,max_sum,crossing_sum)%MOD
