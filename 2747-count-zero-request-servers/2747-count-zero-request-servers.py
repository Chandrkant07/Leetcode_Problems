from typing import List

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # Sort logs by timestamp
        logs.sort(key=lambda item: item[1])
        
        # Pair each query with its original index and sort by query time
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        ans = [0] * len(queries)
        server_counts = [0] * (n + 1)
        active_servers = 0
        
        left = 0
        right = 0
        num_logs = len(logs)
        
        for q_time, orig_idx in sorted_queries:
            # 1. Expand the right boundary of the window (inclusive of q_time)
            while right < num_logs and logs[right][1] <= q_time:
                s_id = logs[right][0]
                if server_counts[s_id] == 0:
                    active_servers += 1
                server_counts[s_id] += 1
                right += 1
            
            # 2. Shrink the left boundary of the window (strictly less than q_time - x)
            while left < num_logs and logs[left][1] < q_time - x:
                s_id = logs[left][0]
                server_counts[s_id] -= 1
                if server_counts[s_id] == 0:
                    active_servers -= 1
                left += 1
            
            # 3. Inactive servers = total servers - active servers in [q_time - x, q_time]
            ans[orig_idx] = n - active_servers
            
        return ans
