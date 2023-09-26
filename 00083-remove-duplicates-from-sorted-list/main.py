from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list_node(l: List) -> Optional[ListNode]:
    if (len(l) == 0):
        return None
    head = ListNode(l[0])
    curr = head
    for x in l[1:]:
        new_node = ListNode(x)
        curr.next = new_node
        curr = curr.next
    return head


def from_list_node_to_list(l: Optional[ListNode]) -> List:
    curr = l
    out = []
    while (curr is not None):
        out.append(curr.val)
        curr = curr.next
    return out


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head is None):
            return None
        cur = head
        nex = head.next
        while (nex is not None):
            if (cur.val == nex.val):
                cur.next = nex.next
                nex = nex.next
            else:
                cur = nex
                nex = nex.next
        return head


sol = Solution()
list_node = create_list_node([1, 2, 2, 2, 2])
ans = sol.deleteDuplicates(head=list_node)
ans = from_list_node_to_list(ans)
print("ans", ans)
