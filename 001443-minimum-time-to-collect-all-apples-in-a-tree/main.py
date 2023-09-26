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


def get_tree(n: int, edges: List[List[int]], hasAppleList: List[bool]) -> TreeNode:
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
        curr_node.level = curr_node.parent.level + \
            1 if curr_node.parent is not None else 0

        visited.add(curr_index)
        for node in curr_node.children:
            node.parent = curr_node
        to_extend = [index for index in ad[curr_index]
                     if index not in visited]
        stack.extend(to_extend)

    return nodes[0]


def fill_previous(node: Optional[TreeNode]):
    if node is None:
        return
    curr = node.parent
    while curr is not None and curr.last_apple_level != curr.level:
        curr.last_apple_level = curr.level
        curr.has_apple = True
        curr = curr.parent


def aux(tree: TreeNode):
    stack = [tree]
    total = 0
    while len(stack) > 0:
        node = stack.pop()
        if node.parent is not None:
            previous_last_apple_level = node.parent.last_apple_level
        else:
            previous_last_apple_level = 0

        if node.has_apple:
            to_add = (node.level - previous_last_apple_level)*2
            total += to_add
            node.last_apple_level = node.level
            fill_previous(node)

        else:
            node.last_apple_level = previous_last_apple_level
            node.has_apple

        for child in node.children:
            stack.append(child)
    return total


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = get_tree(n, edges, hasApple)
        return aux(tree)


n = 90
edges = [[0, 1], [1, 2], [2, 3], [1, 4], [3, 5], [2, 6], [6, 7], [2, 8], [1, 9], [9, 10], [0, 11], [5, 12], [4, 13], [12, 14], [11, 15], [13, 16], [9, 17], [4, 18], [14, 19], [8, 20], [15, 21], [5, 22], [14, 23], [16, 24], [1, 25], [8, 26], [16, 27], [3, 28], [23, 29], [18, 30], [13, 31], [4, 32], [22, 33], [4, 34], [28, 35], [1, 36], [10, 37], [32, 38], [10, 39], [5, 40], [25, 41], [40, 42], [17, 43], [38, 44], [19, 45], [
    13, 46], [33, 47], [13, 48], [15, 49], [21, 50], [17, 51], [4, 52], [4, 53], [44, 54], [53, 55], [33, 56], [42, 57], [23, 58], [29, 59], [32, 60], [35, 61], [47, 62], [3, 63], [21, 64], [38, 65], [34, 66], [45, 67], [29, 68], [50, 69], [51, 70], [22, 71], [61, 72], [33, 73], [42, 74], [28, 75], [33, 76], [31, 77], [3, 78], [51, 79], [40, 80], [55, 81], [31, 82], [34, 83], [24, 84], [9, 85], [80, 86], [21, 87], [74, 88], [56, 89]]
hasApple = [False, True, True, False, False, False, True, True, True, True, False, False, False, True, False, False, False, True, True, True, False, False, False, False, False, False, False, True, True, True, True, False, False, False, False, True, False, True, True, True, False, False, False, True,
            True, True, False, True, True, True, True, False, False, False, False, False, False, True, True, True, True, False, True, False, False, False, False, True, False, False, True, True, False, False, True, True, False, False, False, False, False, True, False, True, False, False, False, True, False, True]
sol = Solution()
ans = sol.minTime(n, edges, hasApple)
print("ans", ans)
