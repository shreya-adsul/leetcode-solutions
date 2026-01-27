class Solution:
    def longestPalindrome(self, s: str) -> str:
        result=""
        for i in range(len(s)):
            left=i
            right=i
            while left>=0 and right<len(s) and s[left]==s[right]:
                    current=s[left:right+1]
                    if len(current)>len(result):
                        result=current
                    left-=1
                    right+=1

            left=i
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                    current=s[left:right+1]
                    if len(current)>len(result):
                        result=current
                    left-=1
                    right+=1
        return result


        