class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash={}
        for ch in s:
            hash[ch]=hash.get(ch,0)+1
        for i, ch in enumerate(s):
            if hash[ch]==1:
                return i
        return -1
        