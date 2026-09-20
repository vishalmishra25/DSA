class Solution(object):
    def twoSum(self, nums, target):
       dic={}
       num=len(nums)
       for i in range(0,num):
        need=target-nums[i]

        if need in dic:
            return[dic[need],i]
        dic[nums[i]]=i    
       
        