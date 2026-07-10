# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         count = 0
#         no_dup = ""

#         for c in s:
#             if c in no_dup:
#                 no_dup = no_dup[: -count + 1]
#                 count = 0

#             elif c not in no_dup:
#                 # print(no_dup)
#                 no_dup += c
#                 count += 1

#         print(no_dup)
#         return len(no_dup) ##66


# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         count = 0
#         no_dup = ""

#         for c in s:
#             if c in no_dup:
#                 idx = no_dup.index(c)
#                 no_dup = no_dup[idx + 1 :]
#             no_dup += c

#             if c not in no_dup:
#                 # print(no_dup)
#                 print("e")
#                 no_dup += c
#                 count += 1

#         print(no_dup)
#        return count     ###83


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count_max = 0
        no_dup = ""

        for c in s:
            if c in no_dup:
                idx = no_dup.index(c)
                no_dup = no_dup[idx + 1:]
                # no_dup += c

            if c not in no_dup:
                # print(no_dup)
                no_dup += c

            if len(no_dup) > count_max:
                # print("entr")
                count_max = len(no_dup)

        # print(f"h{len(no_dup)}h")
        return count_max


s = "abcabcbb"
x = Solution()

print(x.lengthOfLongestSubstring(s))
