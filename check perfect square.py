'''
class Solution:
    def isPerfectSquare(self, n: int) -> bool:
        i = 1
        while(i * i<= n): 
          
        # If (i * i = n) 
            if ((n % i == 0) and (n / i == i)): 
                return True
              
            i = i + 1
        return False
        
'''

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 0
        right = num
        while left<=right:
            mid = (right + left) // 2
            square = mid * mid
            if square == num:
                return True
            if square>num:
                right = mid - 1
            else:
                left = mid + 1
        return left ** 2 == num
