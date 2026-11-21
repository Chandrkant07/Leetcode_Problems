from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}  # char -> closest ancestor index on the current path
        saved = {}
        stack = [(0, 0)]  # (node, state): 0 = enter, 1 = exit
        while stack:
            node, state = stack.pop()
            ch = s[node]
            if state == 0:
                if ch in last:
                    new_parent[node] = last[ch]
                saved[node] = last.get(ch)
                last[ch] = node
                stack.append((node, 1))
                for c in children[node]:
                    stack.append((c, 0))
            else:
                if saved[node] is None:
                    del last[ch]
                else:
                    last[ch] = saved[node]

        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)
        order = []
        st = [0]
        while st:
            u = st.pop()
            order.append(u)
            st.extend(new_children[u])
        size = [1] * n
        for u in reversed(order):
            if u:
                size[new_parent[u]] += size[u]
        return size
