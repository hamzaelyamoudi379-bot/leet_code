class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = ""
        rait = ""
        p = ""
        i = 0
        n = len(s) // 2

        while i < n + 1:
            left += s[i]
            i += 1
        print(left)
        while i > 0:
            rait += s[i]
            i -= 1
        print(rait)

        if left == rait:
            p = p + left
        if left == left[::-1]:
            return left
        elif rait == rait[::-1]:
            return rait

        return p


s = "cbbd"
x = Solution()

print(x.longestPalindrome(s))
