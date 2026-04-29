class Solution(object):
    def reversePrefix(self, word, ch):
    
        index = word.find(ch)
        if index == -1:
            return word
        return word[:index+1][::-1] + word[index+1:]

if __name__ == "__main__":
    sol = Solution()
    print(sol.reversePrefix("abcdefd", "d"))  # Output: "dcbaefd"
    print(sol.reversePrefix("xyxzxe", "z"))   # Output: "zxyxxe"
    print(sol.reversePrefix("abcd", "z"))     # Output: "abcd"