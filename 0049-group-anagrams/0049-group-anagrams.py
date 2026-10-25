class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hash={}
        for str in strs:
            key=''.join(sorted(str))
            if key not in hash:
                hash[key]=[]
            hash[key].append(str)

        return list(hash.values())