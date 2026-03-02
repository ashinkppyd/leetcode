class Solution(object):
    def sumOfUnique(self, nums):
        a=[i for i in nums if nums.count(i)==1]
        b=0
        for c in a:
           b+=c
        return b
    
        