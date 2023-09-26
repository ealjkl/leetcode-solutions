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


def aux(root: Optional[TreeNode], out: List):
    if (root == None):
        return
    curr = root
    out.append(curr.val)
    aux(curr.left, out)
    aux(curr.right, out)


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        aux(root, out)
        return out


root = from_list([1, None, 2, 3, 5, 4, 1, 3, None, 4])
sol = Solution()
ans = sol.preorderTraversal(root)
print("ans", ans)
expected = [1, 2, 3, 4, 4, 1, 5, 3]
