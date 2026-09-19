class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic = {}
        right = 0
        left = 0
        maxi = 0

        while right < len(s):
            if s[right] in dic:
                left = max(left, dic[s[right]] + 1)

            dic[s[right]] = right
            maxi = max(maxi, right - left + 1)

            right += 1

        return maxi 

        
        