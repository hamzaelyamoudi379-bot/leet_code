class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if strs == "":
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

        return prefix


s = Solution()
st = ["flower", "flower", "flower"]


print(s.longestCommonPrefix(st))


# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         string = ""
#         j = len(strs)
#         k = 0
#         i = 0

#         # if j == 1:
#         #     string += strs[0]

#         for s in strs:
#             k = 0
#             while i < j - 1:

#                 if (s[k] in strs[i + 1]) and (s[k] not in string):
#                     # print(s[k])
#                     string += s[k]
#                 k += 1
#                 i += 1

#         return string


# class Solution:
#     def longestCommonPrefix(self, strs: list[str]) -> str:
#         string = ""
#         i = 0

#         for s in strs[i]:
#             if len(strs) == 1:
#                 string += s
#             elif i < len(strs) - 1 and s in strs[i + 1] and s not in string:
#                 string += s
#             i += 1

#         return string


# s = Solution()
# st = s.longestCommonPrefix(["flower", "flow", "flight"])


# print(st)
