class Solution:
    def lengthOfLongestSubstring1(self, s):
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

    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_len, start = 0, 0
        for i, c in enumerate(s):
            while c in char_set:
                print(f"for delete {s[start]}")
                char_set.remove(s[start])
                start += 1
                print(f"start {start}")
            char_set.add(c)
            print(char_set)
            max_len = max(max_len, i - start + 1)
        return max_len


if __name__ == '__main__':
    s = Solution()
    word = "abcaxbcbb"

    res = s.lengthOfLongestSubstring(word)

    print(res)

