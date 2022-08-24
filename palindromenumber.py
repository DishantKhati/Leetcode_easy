class Solution:
    def isPalindrome(self, x: int)->bool:
        w=str(x)
        if w[0]=='-':
            print('false')
        else:            
            y=w[::-1]
            if int(w)==int(y):
                return True
            else:
                return False
