class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0, 0  # sum, count
            
            lsum, lcnt = dfs(node.left)
            rsum, rcnt = dfs(node.right)
            
            total_sum = lsum + rsum + node.val
            total_cnt = lcnt + rcnt + 1
            
            if total_sum // total_cnt == node.val:
                ans += 1
            
            return total_sum, total_cnt
        
        dfs(root)
        return ans