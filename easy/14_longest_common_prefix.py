class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = False


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

    def insert(self, head, word):
        node = head

        for character in word:
            node = node.children.setdefault(character, TrieNode())

        node.is_leaf = True

    def longest_common_prefix_trie(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        head = TrieNode()
        for word in strs:
            self.insert(head, word)

        lcp = ""
        node = head

        while node.is_leaf == False and len(node.children) == 1:
            for character, next_node in node.children.items():
                lcp += character
                node = next_node

        return lcp


if __name__ == '__main__':
    s = Solution()
    strs = ["flower", "flow", "flight"]
    # res = s.longest_common_prefix(strs)

    res = s.longest_common_prefix_trie(strs)

    print(res)
