from __future__ import annotations
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, index: int, children: List[TreeNode] = None, has_apple: bool = False, parent: Optional[TreeNode] = None, level: int = 0) -> None:
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
    ad = [[] for _ in range(n)]

    for index1, index2 in edges:
        ad[index1].append(index2)
        ad[index2].append(index1)

    stack = [0]
    visited = set()
    while len(stack) > 0:
        curr_index = stack.pop()
        curr_node = nodes[curr_index]
        curr_node.children = [nodes[idx]
                              for idx in ad[curr_index] if idx not in visited]
        visited.add(curr_index)
        for node in curr_node.children:
            node.parent = curr_node
        to_extend = [index for index in ad[curr_index]
                     if index not in visited]
        stack.extend(to_extend)

        # print(curr_node.index, [n.index for n in curr_node.children])

        # print(curr_node.index,
        #       curr_node.parent.index if curr_node.parent is not None else None)

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
            to_add = (node.level - previous_last_apple_level)*2
            print(node.index, to_add)
            total += to_add
            node.last_apple_level = node.level
            if node.parent is not None:
                node.parent.last_apple_level = node.parent.level
                for child in node.parent.children:
                    child.last_apple_level = node.parent.level
        else:
            node.last_apple_level = previous_last_apple_level
            print(node.index, 0)

        for child in node.children:
            queue.append(child)
    return total


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = build_tree(n, edges, hasApple)
        return aux(tree)


n = 40
edges = [[0, 1], [0, 2], [0, 3], [3, 4], [1, 5], [5, 6], [1, 7], [2, 8], [1, 9], [6, 10], [6, 11], [8, 12], [4, 13], [8, 14], [4, 15], [15, 16], [10, 17], [3, 18], [6, 19], [10, 20], [
    1, 21], [0, 22], [0, 23], [9, 24], [23, 25], [19, 26], [10, 27], [14, 28], [12, 29], [10, 30], [12, 31], [4, 32], [4, 33], [20, 34], [29, 35], [7, 36], [16, 37], [13, 38], [34, 39]]
hasApple = [True, True, True, False, False, True, False, False, True, False, True, False, True, False, True, False, True, True, False,
            True, False, True, True, False, True, False, False, False, False, False, False, True, False, True, False, False, False, False, True, True]
sol = Solution()
ans = sol.minTime(n, edges, hasApple)
print("ans", ans)
