class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def merge_two_lists(self, list1, list2):
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1 is not None:
            current.next = list1
        else:
            current.next = list2
        return head.next


list1 = ListNode(1, ListNode(2, ListNode(4, ListNode(6, ListNode(8)))))
list2 = ListNode(2, ListNode(3, ListNode(4)))
head = ListNode().merge_two_lists(list1, list2)
while head is not None:
    print(head.val)
    head = head.next
