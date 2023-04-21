class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            max_result = 0
        else:
            max_result = 1

        for i in range(len(s)-1):
            substr=s[i]
            for j in range(i+1, len(s)):
                if s[j] not in s[i:j]:
                    substr += s[j]
                    if max_result <= j-i+1:
                        max_result = j-i+1
                else:
                    break

        return max_result


if __name__ == '__main__':
    s = Solution()
    word = "abcaxbcbb"

    res = s.lengthOfLongestSubstring(word)

    print(res)

