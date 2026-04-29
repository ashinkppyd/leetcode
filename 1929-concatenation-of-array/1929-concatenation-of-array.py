class Solution(object):
    def getConcatenation(self, nums):
        ans = nums + nums
        return ans


if __name__ == "__main__":
    nums = [1, 2, 1]
    sol = Solution()
    result = sol.getConcatenation(nums)
    print(result)  
       
        