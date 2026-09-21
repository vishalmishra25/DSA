class Solution(object):
    def reverseString(self, s):
        def reverseString(left , right):
            if left>=right:
                return
            s[left],s[right]=s[right],s[left]
            reverseString(left+1,right-1)
        reverseString(0,len(s)-1)       
        
        