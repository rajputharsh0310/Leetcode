class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m=len(s)
        n=len(t)
        if m<n:
            return ""
        target={}
        for ch in t:
            target[ch]=target.get(ch,0)+1
        window={}
        min_len=float("inf")
        left=0
        answer=""
        for right in range(m):
            ch=s[right]
            window[ch]=window.get(ch,0)+1
            valid=True
            for ch in target:
                if window.get(ch,0)<target[ch]:
                    valid=False
                    break
            while valid:
                if right-left+1<min_len:
                    min_len=right-left+1
                    answer=s[left:right+1]
                left_ch=s[left]
                window[left_ch]-=1
                if window[left_ch]==0:
                    del window[left_ch]
                left+=1
                for ch in target:
                    if window.get(ch,0)<target[ch]:
                        valid=False
                        break
        return answer