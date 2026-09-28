class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        n=len(s)
        left=0
        count=0
        m=0
        for right in range(n):
            m+=abs(ord(s[right])-ord(t[right]))
            while m>maxCost:
                m-=abs(ord(s[left])-ord(t[left]))
                left+=1
            count=max(count,right-left+1)
        return count