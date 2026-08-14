import collections

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        # Use a dictionary to store character frequencies in the current window
        freq = collections.defaultdict(int) 

        for right in range(len(s)):
            char_r = s[right]
            freq[char_r] += 1 # Add current character to window

            # If the current character's frequency exceeds 2,
            # shrink the window from the left until it's valid again.
            while freq[char_r] > 2:
                char_l = s[left]
                freq[char_l] -= 1 # Remove character at left pointer
                left += 1          # Move left pointer
            
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
        
        return max_len
