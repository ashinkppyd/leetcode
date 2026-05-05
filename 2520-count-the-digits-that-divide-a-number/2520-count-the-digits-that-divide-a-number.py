class Solution(object):
    def countDigits(self, num):
        count = 0
        
        for d in str(num):
            digit = int(d)
            if num % digit == 0:
                count += 1
        
        return count



    
        