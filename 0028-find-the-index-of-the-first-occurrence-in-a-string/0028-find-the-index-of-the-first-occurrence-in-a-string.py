class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_haystack = len(haystack)
        len_needle = len(needle)

        # Handle edge case where needle is empty (returns 0 by convention)
        if len_needle == 0:
            return 0

        # Iterate through possible starting positions for needle in haystack
        for i in range(len_haystack - len_needle + 1):
            # This is where you need to implement the logic
            # to check if haystack[i : i + len_needle] == needle.
            # If a match is found, return i.
            
            # Example placeholder (replace with actual comparison logic):
            if haystack[i:i+len_needle] == needle:
                return i
        
        # If the loop completes and no match is found
        return -1