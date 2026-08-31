class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = -1
        last = -1
        prev_critical = -1
        min_distance = float('inf')

        prev = head
        curr = head.next
        index = 1

        while curr and curr.next:
            if ((curr.val > prev.val and curr.val > curr.next.val) or
                (curr.val < prev.val and curr.val < curr.next.val)):

                if first == -1:
                    first = index
                else:
                    min_distance = min(min_distance, index - prev_critical)

                prev_critical = index
                last = index

            prev = curr
            curr = curr.next
            index += 1

        if first == -1 or first == last:
            return [-1, -1]

        return [min_distance, last - first]