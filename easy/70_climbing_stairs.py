class Solution:
    def climb_stairs(self, n: int) -> int:
        """
        :param n: int
        :return: prev: int

        Main idea is to find the regularity.
        There are next stairs combination count is equal to sum of the two previous stairs combinations count:)
        """
        prev = 1
        prev_prev = 0
        for i in range(1, n + 1):
            current = prev + prev_prev
            prev_prev = prev
            prev = current

        return prev


if __name__ == '__main__':
    s = Solution()
    n = 5
    res = s.climb_stairs(n)

    print(res)
