from __future__ import annotations
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, index: int, children: List = None, has_apple: bool = False, parent: Optional[TreeNode] = None, level: int = 0) -> None:
        if (children is None):
            children = []
        self.index = index
        self.children = children
        self.has_apple = has_apple
        self.parent = parent
        self.last_apple_level = -1
        self.level = level


def build_tree(n: int, edges: List[List[int]], hasAppleList: List[bool]) -> TreeNode:
    nodes = [
        TreeNode(i, children=[], has_apple=hasAppleList[i]) for i in range(n)
    ]

    for parent, child in edges:
        nodes[parent].children.append(nodes[child])
        nodes[child].parent = nodes[parent]

    return nodes[0]


def aux(tree: TreeNode):
    queue = deque([tree])
    total = 0
    while len(queue) > 0:
        node = queue.popleft()
        node.level = node.parent.level + 1 if node.parent is not None else 0
        if node.parent is not None:
            previous_last_apple_level = node.parent.last_apple_level
        else:
            previous_last_apple_level = 0

        if node.has_apple:
            total += (node.level - previous_last_apple_level)*2
            node.last_apple_level = node.level
            if node.parent is not None:
                node.parent.last_apple_level = node.parent.level
        else:
            node.last_apple_level = previous_last_apple_level

        for child in node.children:
            queue.append(child)
    return total


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = build_tree(n, edges, hasApple)
        return aux(tree)


n = 4
edges = [[0, 2], [0, 3], [2, 1]]
hasApple = [False, True, False, False]
sol = Solution()
ans = sol.minTime(n, edges, hasApple)
print("ans", ans)
