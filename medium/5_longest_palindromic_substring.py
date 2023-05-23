class VerySlowSolution(object):
    def is_palindrome(self, substring):
        """
        :param substring:
        :return: boolean
        """
        for i in range(len(substring) // 2):
            if substring[i] != substring[-i - 1]:
                return False

        return True

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for l in range(len(s)):
            for r in range(l + 1, len(s) + 1):
                substr = (s[l:r])
                if self.is_palindrome(substr) and len(substr) > len(res):
                    res = substr
        return res


class Solution(object):
    def expandAroundCenter(self, s, left, right):
        L = left
        R = right
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return R - L - 1

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]


if __name__ == '__main__':
    solution = Solution()
    s = "babab"
    print(solution.longestPalindrome(s))
