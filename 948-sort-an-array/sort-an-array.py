class Solution(object):
    def sortArray(self, nums):

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        Left = nums[mid:]
        Right = nums[:mid]

        left = self.sortArray(Left)
        right = self.sortArray(Right)

        result = []

        i = 0
        j = 0

        n = len(left)
        m = len(right)

        while i < n and j < m:

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1

        while i < n:
            result.append(left[i])
            i += 1

        while j < m:
            result.append(right[j])
            j += 1

        return result