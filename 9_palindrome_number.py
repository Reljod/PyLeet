"""
Problem: https://leetcode.com/problems/palindrome-number/
"""

class Solution:

    def is_palindrome(self, x: int) -> bool:
        if (x < 0):
            return False
    
        div = 1
        while x >= 10*div:
            div *= 10
            
        while div >= 1:
            
            last_digit = x % 10
            first_digit = x // div
            
            if first_digit != last_digit:
                return False

            x = (x % div) // 10
            div /= 100
        
        return True
        
if __name__ == '__main__':
    print(Solution().is_palindrome(982))
    print(Solution().is_palindrome(12321))
    print(Solution().is_palindrome(121))
        