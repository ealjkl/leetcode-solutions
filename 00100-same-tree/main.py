from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def from_list(elements):
    root_node = TreeNode(val=elements[0])
    nodes = [root_node]
    for i, x in enumerate(elements[1:]):
        if x is None:
            continue
        parent_node = nodes[i // 2]
        is_left = (i % 2 == 0)
        node = TreeNode(val=x)
        if is_left:
            parent_node.left = node
        else:
            parent_node.right = node
        nodes.append(node)

    return root_node


def are_nodes_equal(n1: Optional[TreeNode], n2: Optional[TreeNode]):
    if n1 is None:
        return n2 is None
    if n2 is None:
        return n1 is None
    return n1.val == n2.val


def aux(tree1: Optional[TreeNode], tree2: Optional[TreeNode]):
    # if (tree1 == None):
    #     return
    stack1 = [tree1]
    stack2 = [tree2]
    while len(stack1) > 0 and len(stack2) > 0:
        curr1 = stack1.pop()
        curr2 = stack2.pop()
        if (not are_nodes_equal(curr1, curr2)):
            return False
        if (curr1 is not None):
            stack1.extend([curr1.left, curr1.right])
        if (curr2 is not None):
            stack2.extend([curr2.left, curr2.right])

    return len(stack1) == 0 and len(stack2) == 0


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return aux(p, q)


p = from_list([1, 2, 3])
q = from_list([1, 2, 4])
sol = Solution()
ans = sol.isSameTree(p, q)
print("ans", ans)
