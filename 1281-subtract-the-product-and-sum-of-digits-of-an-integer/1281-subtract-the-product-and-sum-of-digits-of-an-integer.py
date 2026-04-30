class Solution(object):
    def subtractProductAndSum(self, n):
        m = 1
        sum = 0
        
        while n > 0:
            digit = n % 10
            m *= digit
            sum += digit
            n //= 10
            
        return m - sum
        