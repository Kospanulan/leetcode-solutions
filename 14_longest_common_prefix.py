class Solution:
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length_of_shortest_word = len(strs[0])
        for s in strs:
            if len(s) < length_of_shortest_word:
                length_of_shortest_word = len(s)

        prefix = ""
        for i in range(length_of_shortest_word):
            current_letter = strs[0][i:i + 1]
            for s in strs:
                if s[i:i + 1] != current_letter:
                    return prefix
            prefix += current_letter
        return prefix


if __name__ == '__main__':
    s = Solution()
    strs = ["flower", "flow", "flight"]
    res = s.longest_common_prefix(strs)

    print(res)
