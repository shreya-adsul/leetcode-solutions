class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        s1=set()
        max_length=0
        while right<len(s):
            if s[right]  not in s1:
                s1.add(s[right])
                right+=1
                max_length=max(max_length,right-left)
            else:
                s1.remove(s[left])
                left+=1
        return max_length
