class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = roman[s[-1]]
        for i in reversed(range(len(s)-1)):
            if roman[s[i]] >= roman[s[i + 1]]:
                result += roman[s[i]]
            else:
                result -= roman[s[i]]
        return result


if __name__ == '__main__':
    s = Solution()
    roman = "MCMXCIV"
    result = s.romanToInt(roman)

    print(result)
