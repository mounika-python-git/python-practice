
class Solution:
    def isPalindrome(self,s):
        
        if s==s[::-1]:
            return True
                
        else:
            return False

s=input()
obj=Solution()
print(obj.isPalindrome(s))
    
    
        
