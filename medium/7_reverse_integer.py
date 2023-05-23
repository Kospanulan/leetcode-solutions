class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        string_x = str(x)
        reversed_string_x = string_x[::-1]
        if x >= 0:
            res = int(reversed_string_x)
        else:
            res = int('-' + reversed_string_x[:-1])

        if res >= 2 ** 31 - 1 or res <= -2 ** 31:
            return 0

        return res


if __name__ == '__main__':
    solution = Solution()
    x = 123
    print(solution.reverse(x))
