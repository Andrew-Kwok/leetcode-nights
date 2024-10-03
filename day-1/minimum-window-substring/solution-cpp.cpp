class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> character_count;
        int bad_count = 0;

        // Initialize bad_count and character_count for string t
        for (char c : t) {
            bad_count++;
            character_count[c]--;
        }

        int best_l = -INT_MAX, best_r = -1;
        int l = 0;

        for (int r = 0; r < s.size(); r++) {
            if (character_count[s[r]] < 0) {
                bad_count--;
            }
            character_count[s[r]]++;

            // Adjust the left pointer to shrink the window
            while (bad_count == 0 && character_count[s[l]] > 0) {
                character_count[s[l]]--;
                l++;
            }

            // Update best_l and best_r for the smallest window
            if (bad_count == 0 && best_r - best_l > r - l) {
                best_l = l;
                best_r = r;
            }
        }

        if (best_r == -1) {
            return "";
        }
        return s.substr(best_l, best_r - best_l + 1);
    }
};

