class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        fre={}
        for i in range(0,n+1):
            fre[i]=0
        for num in nums:
            fre[num]=1
        for k,v in fre.items():
            if v==0:
             return k        
           
            



        
        