class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self, val, next=None):
        if not isinstance(val, int):
            val = int(val)
        self.head = ListNode(val, next)
        self._last_node = self.head

    def insert(self, val):
        if not isinstance(val, int):
            val = int(val)

        self._last_node.next = ListNode(val)
        self._last_node = self._last_node.next

    def get_head(self):
        return self.head


class Solution(object):

    def get_number_from_linked_list(self, node):
        number = ""
        while node:
            number = number + str(node.val)
            node = node.next

        return int(number[::-1])

    def get_linked_list_from_number(self, number):
        number = str(number)[::-1]
        head = LinkedList(int(number[0]))
        # node = head
        for i in range(1, len(number)):
            head.insert(number[i])

        return head.get_head()

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        number_1 = self.get_number_from_linked_list(l1)
        number_2 = self.get_number_from_linked_list(l2)

        result_number = number_1 + number_2

        result = self.get_linked_list_from_number(result_number)

        return result



def get_sum(l1 ,l2):
    num_str_1 = [str(x) for x in l1[::-1]]
    num_str_2 = [str(x) for x in l2[::-1]]

    num1 = int("".join(num_str_1))
    num2 = int("".join(num_str_2))
    print(f"num1: {num1}")
    print(f"num2: {num2}")

    expected = num1 + num2

    return str(expected)[::-1]


if __name__ == '__main__':
    so = Solution()
    l1 = [0, 8, 6, 5, 6, 8, 3, 5, 7]
    head_1 = LinkedList(l1[0])
    for i in range(1, len(l1)):
        head_1.insert(l1[i])

    l2 = [6, 7, 8, 0, 8, 5, 8, 9, 7]
    head_2 = LinkedList(l2[0])
    for i in range(1, len(l2)):
        head_2.insert(l2[i])

    res = so.addTwoNumbers(head_1.get_head(), head_2.get_head())

    got_res = 0
    while res:
        got_res = got_res * 10 + res.val
        print(res.val)
        res = res.next

    print(f"got_res:  {got_res}, \n"
          f"expected: {get_sum(l1, l2)}")

