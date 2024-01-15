# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
#
#
#
# Example 1:
#
# Input: s = "hello"
# Output: "holle"
# Example 2:
#
# Input: s = "leetcode"
# Output: "leotcede"
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        s_list = list(s)
        start = 0
        end = len(s) - 1
        wowels = 'aeiouAEIOU'
        while start < end:

            if s_list[start] in wowels and s_list[end] in wowels:

                s_list[start], s_list[end] = s_list[end], s_list[start]

                start += 1; end -= 1

            elif s_list[start] not in wowels:
                start += 1

            elif s_list[end] not in wowels:
                end -= 1

        return ''.join(s_list)
obj=Solution()
result=obj.reverseVowels("hello")

