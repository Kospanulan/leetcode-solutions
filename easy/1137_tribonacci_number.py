class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 2:
            return 1
        elif n == 1:
            return 1
        elif n == 0:
            return 0

        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)


if __name__ == '__main__':
    s = Solution()
    n = 25
    res = s.tribonacci(n)

    print(res)
