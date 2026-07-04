class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        no_dup = ""
        ind = 0

        for c in s:
            print(c)
            if c in no_dup:
                print(no_dup)
                no_dup = no_dup[-count:]
                count = 0

            elif c not in no_dup:
                # print(no_dup)
                no_dup += c
                count += 1

        return count


s = "abcabcbb"
x = Solution()

print(x.lengthOfLongestSubstring(s))
