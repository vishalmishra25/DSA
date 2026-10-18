class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n = len(nums)
        count = 0
        maxcount = 0

        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                maxcount = max(maxcount, count)
                count = 0

        return max(maxcount, count)
       
        