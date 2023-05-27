class Solution:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 0:
            return 0

        return self.fib(n-1) + self.fib(n-2)


if __name__ == '__main__':
    s = Solution()
    n = 4
    res = s.fib(n)

    print(res)
