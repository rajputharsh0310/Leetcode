class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        target={}
        for ch in s:
            target[ch]=target.get(ch,0)+1
        to_match={}
        for ch in t:
            to_match[ch]=to_match.get(ch,0)+1
        for ch in target:
            if ch not in to_match or target[ch]>to_match[ch]:
                return False
        return True
        