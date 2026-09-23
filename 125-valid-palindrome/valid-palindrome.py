class Solution(object):
    def isPalindrome(self, s):
                s = ''.join(c.lower() for c in s if c.isalnum())

                def check (l,r):
                    if l>=r:
                        return True  
                    if s[l]!=s[r]:
                        return False 
                    return check (l+1,r-1)
                return check(0,len(s)-1)           
             
           
        
        