# 3483. Unique 3-Digit Even Numbers

**Difficulty:** Easy

## Solution

```python
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen = set()
        n = len(digits)

        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 != 0:
                        continue
                    seen.add(digits[i] * 100 + digits[j] * 10 + digits[k])

        return len(seen)
```
