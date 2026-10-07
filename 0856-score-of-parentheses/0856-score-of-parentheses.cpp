#include <string>
#include <algorithm>

class Solution {
public:
    int scoreOfParentheses(std::string s) {
        int score = 0;
        int depth = 0;
        int n = s.length();

        for (int i = 0; i < n; i++) {
            if (s[i] == '(') {
                depth++;
            } else {
                depth--; // Decrement depth to match the current layer
                // If the previous character was '(', we found an innermost "()"
                if (s[i - 1] == '(') {
                    score += (1 << depth); 
                }
            }
        }
        return score;
    }
};
